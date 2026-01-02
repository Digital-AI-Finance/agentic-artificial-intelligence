# Exercise L07: Building a Corrective RAG (CRAG) System

**Week 7 - Advanced RAG**

## Overview

Implement a Corrective Retrieval-Augmented Generation (CRAG) system that evaluates retrieval quality and takes corrective actions, improving answer reliability over naive RAG.

## Learning Objectives

- **Primary (Apply)**: Implement retrieval quality evaluation with confidence scoring
- **Secondary (Create)**: Design fallback strategies for poor retrieval scenarios
- **Tertiary (Evaluate)**: Assess CRAG effectiveness against baseline RAG

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Vector store (chromadb, FAISS, or similar)
- Understanding of basic RAG architecture

## Problem Statement

Standard RAG has a critical weakness: it always retrieves and uses documents, even when:
- The query is out of domain (no relevant documents exist)
- Retrieved documents are marginally relevant
- The retrieval system returns noise

CRAG addresses this by adding an evaluation layer that assesses retrieval quality and routes to appropriate handlers:
- **Correct**: High-quality retrieval -> use documents directly
- **Ambiguous**: Partial match -> refine query and re-retrieve
- **Incorrect**: Poor retrieval -> fall back to web search or direct LLM

This exercise develops skills in building self-correcting retrieval systems.

### Part 1: Retrieval Evaluator (35 points)

Implement a lightweight evaluator that scores retrieval quality:

**1a: Evaluation Result Schema (10 points)**
```python
from dataclasses import dataclass
from typing import Literal
from enum import Enum

class RetrievalAction(Enum):
    CORRECT = "correct"      # Use documents directly
    AMBIGUOUS = "ambiguous"  # Refine and retry
    INCORRECT = "incorrect"  # Fall back to web search

@dataclass
class EvaluationResult:
    action: RetrievalAction
    confidence: float        # 0.0 to 1.0
    reasoning: str           # Explanation for the decision
    relevant_docs: list[int] # Indices of relevant documents

    @property
    def is_usable(self) -> bool:
        """Check if retrieval is usable (correct or ambiguous with some relevant docs)."""
        return self.action != RetrievalAction.INCORRECT
```

**1b: Retrieval Evaluator Implementation (25 points)**
```python
from typing import Protocol

class Document(Protocol):
    content: str
    metadata: dict

class RetrievalEvaluator:
    def __init__(self, llm_client, threshold_correct: float = 0.7, threshold_ambiguous: float = 0.3):
        self.llm = llm_client
        self.threshold_correct = threshold_correct
        self.threshold_ambiguous = threshold_ambiguous

    def evaluate(self, query: str, documents: list[Document]) -> EvaluationResult:
        """
        Evaluate retrieval quality for a query-document set.

        Args:
            query: The user's query
            documents: Retrieved documents to evaluate

        Returns:
            EvaluationResult with action, confidence, and reasoning
        """
        if not documents:
            return EvaluationResult(
                action=RetrievalAction.INCORRECT,
                confidence=0.0,
                reasoning="No documents retrieved",
                relevant_docs=[]
            )

        # Score each document's relevance
        doc_scores = []
        for i, doc in enumerate(documents):
            score = self._score_document(query, doc)
            doc_scores.append((i, score))

        # Calculate aggregate confidence
        scores = [s for _, s in doc_scores]
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)

        # Use max score for action decision (at least one good doc)
        confidence = max_score

        # Determine action based on thresholds
        if confidence >= self.threshold_correct:
            action = RetrievalAction.CORRECT
            reasoning = f"High-quality retrieval (confidence: {confidence:.2f})"
        elif confidence >= self.threshold_ambiguous:
            action = RetrievalAction.AMBIGUOUS
            reasoning = f"Partial match (confidence: {confidence:.2f}), consider query refinement"
        else:
            action = RetrievalAction.INCORRECT
            reasoning = f"Poor retrieval (confidence: {confidence:.2f}), falling back to web search"

        # Mark relevant documents (above ambiguous threshold)
        relevant_docs = [i for i, s in doc_scores if s >= self.threshold_ambiguous]

        return EvaluationResult(
            action=action,
            confidence=confidence,
            reasoning=reasoning,
            relevant_docs=relevant_docs
        )

    def _score_document(self, query: str, document: Document) -> float:
        """Score a single document's relevance to the query."""
        prompt = f"""Rate how relevant this document is to the query on a scale of 0.0 to 1.0.

Query: {query}

Document:
{document.content[:1000]}

Respond with only a number between 0.0 and 1.0.
"""
        response = self.llm.complete(prompt)
        try:
            score = float(response.strip())
            return max(0.0, min(1.0, score))
        except ValueError:
            return 0.5  # Default to ambiguous if parsing fails
```

**Scoring Thresholds:**
| Score Range | Action | Interpretation |
|-------------|--------|----------------|
| >= 0.7 | CORRECT | At least one document is highly relevant |
| 0.3 - 0.7 | AMBIGUOUS | Partial relevance, may need refinement |
| < 0.3 | INCORRECT | No relevant documents, use fallback |

### Part 2: Corrective Actions (35 points)

Implement handlers for each evaluation outcome:

**2a: Correct Handler (10 points)**
```python
class CRAGPipeline:
    def __init__(self, retriever, evaluator: RetrievalEvaluator, llm_client):
        self.retriever = retriever
        self.evaluator = evaluator
        self.llm = llm_client
        self.web_search = WebSearchFallback()  # Implement or simulate

    def handle_correct(self, query: str, docs: list[Document], eval_result: EvaluationResult) -> str:
        """
        Use retrieved documents directly for generation.
        Filter to only relevant documents based on evaluation.
        """
        # Use only the documents marked as relevant
        relevant_docs = [docs[i] for i in eval_result.relevant_docs]

        # Build context from relevant documents
        context = "\n\n---\n\n".join([
            f"Source {i+1}:\n{doc.content}"
            for i, doc in enumerate(relevant_docs)
        ])

        prompt = f"""Answer the question based on the following context.
Cite specific sources when possible.

Context:
{context}

Question: {query}

Answer:"""

        return self.llm.complete(prompt)
```

**2b: Ambiguous Handler (15 points)**
```python
    def handle_ambiguous(self, query: str, docs: list[Document], eval_result: EvaluationResult) -> str:
        """
        Refine the query and re-retrieve.
        If still ambiguous after refinement, use available documents.
        """
        # Step 1: Generate refined query
        refinement_prompt = f"""The following query returned partially relevant results.
Suggest a more specific query that might retrieve better results.

Original query: {query}

Retrieved content snippets:
{self._get_snippets(docs, max_chars=500)}

Refined query (be more specific):"""

        refined_query = self.llm.complete(refinement_prompt).strip()

        # Step 2: Re-retrieve with refined query
        new_docs = self.retriever.retrieve(refined_query, k=5)

        # Step 3: Re-evaluate
        new_eval = self.evaluator.evaluate(refined_query, new_docs)

        # Step 4: Route based on new evaluation
        if new_eval.action == RetrievalAction.CORRECT:
            return self.handle_correct(refined_query, new_docs, new_eval)
        elif new_eval.action == RetrievalAction.AMBIGUOUS:
            # Use what we have - combine original relevant docs with new
            combined_docs = self._combine_docs(docs, new_docs, eval_result, new_eval)
            return self._generate_with_uncertainty(query, combined_docs)
        else:
            # Refinement didn't help, fall back
            return self.handle_incorrect(query, docs, new_eval)

    def _get_snippets(self, docs: list[Document], max_chars: int = 500) -> str:
        """Extract snippets from documents."""
        snippets = []
        for doc in docs[:3]:  # Top 3
            snippet = doc.content[:max_chars] + "..." if len(doc.content) > max_chars else doc.content
            snippets.append(snippet)
        return "\n---\n".join(snippets)

    def _combine_docs(self, docs1, docs2, eval1, eval2) -> list[Document]:
        """Combine relevant documents from both retrieval attempts."""
        combined = []
        seen_content = set()

        for i in eval1.relevant_docs:
            if docs1[i].content not in seen_content:
                combined.append(docs1[i])
                seen_content.add(docs1[i].content)

        for i in eval2.relevant_docs:
            if docs2[i].content not in seen_content:
                combined.append(docs2[i])
                seen_content.add(docs2[i].content)

        return combined

    def _generate_with_uncertainty(self, query: str, docs: list[Document]) -> str:
        """Generate answer while expressing uncertainty due to limited evidence."""
        context = "\n\n".join([doc.content for doc in docs])
        prompt = f"""Answer the question based on the following context.
Note: The available information may be incomplete. Express uncertainty where appropriate.

Context:
{context}

Question: {query}

Answer (noting any limitations):"""

        return self.llm.complete(prompt)
```

**2c: Incorrect Handler (10 points)**
```python
    def handle_incorrect(self, query: str, docs: list[Document], eval_result: EvaluationResult) -> str:
        """
        Fall back to web search or direct LLM response.
        """
        # Try web search first
        try:
            web_results = self.web_search.search(query, num_results=3)
            if web_results:
                context = "\n\n".join([
                    f"Web Source ({r['url']}):\n{r['snippet']}"
                    for r in web_results
                ])

                prompt = f"""Answer the question based on web search results.
Cite sources when possible.

Web Results:
{context}

Question: {query}

Answer:"""

                return self.llm.complete(prompt)
        except Exception as e:
            pass  # Fall through to direct LLM

        # Direct LLM as last resort
        prompt = f"""I don't have specific documents about this topic.
Answer to the best of your knowledge, but clearly indicate this is from general knowledge, not specific sources.

Question: {query}

Answer (from general knowledge):"""

        return self.llm.complete(prompt)

class WebSearchFallback:
    """Simulated web search (replace with real API in production)."""

    def search(self, query: str, num_results: int = 3) -> list[dict]:
        # Simulate web search results
        # In production, use Tavily, Serper, or similar
        return [
            {"url": "https://example.com/1", "snippet": f"Information about {query}..."},
            {"url": "https://example.com/2", "snippet": f"More details on {query}..."},
        ]
```

### Part 3: Full CRAG Pipeline (30 points)

Assemble the complete pipeline with metrics tracking:

**3a: Pipeline Integration (15 points)**
```python
@dataclass
class CRAGResult:
    answer: str
    action_taken: RetrievalAction
    confidence: float
    num_docs_used: int
    query_refined: bool
    fallback_used: bool
    metrics: dict

class CRAGPipeline:
    # ... (previous methods)

    def run(self, query: str) -> CRAGResult:
        """Execute the full CRAG pipeline."""
        metrics = {"retrieval_time": 0, "eval_time": 0, "generation_time": 0}

        # Step 1: Initial retrieval
        start = time.time()
        docs = self.retriever.retrieve(query, k=5)
        metrics["retrieval_time"] = time.time() - start

        # Step 2: Evaluate retrieval quality
        start = time.time()
        eval_result = self.evaluator.evaluate(query, docs)
        metrics["eval_time"] = time.time() - start

        # Step 3: Route to appropriate handler
        start = time.time()
        query_refined = False
        fallback_used = False

        if eval_result.action == RetrievalAction.CORRECT:
            answer = self.handle_correct(query, docs, eval_result)
        elif eval_result.action == RetrievalAction.AMBIGUOUS:
            answer = self.handle_ambiguous(query, docs, eval_result)
            query_refined = True
        else:
            answer = self.handle_incorrect(query, docs, eval_result)
            fallback_used = True

        metrics["generation_time"] = time.time() - start

        return CRAGResult(
            answer=answer,
            action_taken=eval_result.action,
            confidence=eval_result.confidence,
            num_docs_used=len(eval_result.relevant_docs),
            query_refined=query_refined,
            fallback_used=fallback_used,
            metrics=metrics
        )
```

**3b: Evaluation Suite (15 points)**

Create a test suite with diverse queries:

```python
@dataclass
class TestCase:
    query: str
    expected_action: RetrievalAction
    category: str  # "in_domain", "partial", "out_of_domain"
    has_ground_truth: bool
    ground_truth: str | None = None

test_cases = [
    # In-domain queries (should be CORRECT)
    TestCase("What is the capital of France?", RetrievalAction.CORRECT, "in_domain", True, "Paris"),
    TestCase("Explain photosynthesis", RetrievalAction.CORRECT, "in_domain", False),
    TestCase("Who wrote Romeo and Juliet?", RetrievalAction.CORRECT, "in_domain", True, "William Shakespeare"),

    # Partial match queries (should be AMBIGUOUS)
    TestCase("Compare machine learning to traditional programming", RetrievalAction.AMBIGUOUS, "partial", False),
    TestCase("What are the implications of quantum computing?", RetrievalAction.AMBIGUOUS, "partial", False),

    # Out-of-domain queries (should be INCORRECT)
    TestCase("What is the meaning of xyzzy in the context of plugh?", RetrievalAction.INCORRECT, "out_of_domain", False),
    TestCase("Describe the fictional planet Zorgon-7", RetrievalAction.INCORRECT, "out_of_domain", False),

    # Edge cases
    TestCase("", RetrievalAction.INCORRECT, "edge_case", False),  # Empty query
    TestCase("???", RetrievalAction.INCORRECT, "edge_case", False),  # Nonsense
    TestCase("the the the", RetrievalAction.INCORRECT, "edge_case", False),  # Repeated words
]

def run_evaluation(pipeline: CRAGPipeline, test_cases: list[TestCase]) -> dict:
    """Run evaluation suite and compute metrics."""
    results = []

    for tc in test_cases:
        result = pipeline.run(tc.query)

        # Check if action matches expected
        action_correct = result.action_taken == tc.expected_action

        # Check answer quality if ground truth exists
        answer_correct = None
        if tc.has_ground_truth and tc.ground_truth:
            answer_correct = tc.ground_truth.lower() in result.answer.lower()

        results.append({
            "query": tc.query,
            "category": tc.category,
            "expected_action": tc.expected_action.value,
            "actual_action": result.action_taken.value,
            "action_correct": action_correct,
            "confidence": result.confidence,
            "answer_correct": answer_correct,
            "fallback_used": result.fallback_used,
            "metrics": result.metrics
        })

    # Compute aggregate metrics
    action_accuracy = sum(r["action_correct"] for r in results) / len(results)
    avg_confidence = sum(r["confidence"] for r in results) / len(results)
    fallback_rate = sum(r["fallback_used"] for r in results) / len(results)

    # Per-category accuracy
    categories = set(r["category"] for r in results)
    category_accuracy = {}
    for cat in categories:
        cat_results = [r for r in results if r["category"] == cat]
        category_accuracy[cat] = sum(r["action_correct"] for r in cat_results) / len(cat_results)

    return {
        "results": results,
        "action_accuracy": action_accuracy,
        "avg_confidence": avg_confidence,
        "fallback_rate": fallback_rate,
        "category_accuracy": category_accuracy,
        "answer_accuracy": sum(1 for r in results if r["answer_correct"] is True) /
                          sum(1 for r in results if r["answer_correct"] is not None)
    }
```

## Comparison: CRAG vs Naive RAG

Implement a baseline for comparison:

```python
class NaiveRAGPipeline:
    """Standard RAG without retrieval evaluation."""

    def __init__(self, retriever, llm_client):
        self.retriever = retriever
        self.llm = llm_client

    def run(self, query: str) -> str:
        """Always retrieve and use documents."""
        docs = self.retriever.retrieve(query, k=5)
        context = "\n\n".join([doc.content for doc in docs])

        prompt = f"""Answer based on the context.

Context:
{context}

Question: {query}

Answer:"""

        return self.llm.complete(prompt)
```

**Comparison Metrics:**
| Metric | Naive RAG | CRAG | Notes |
|--------|-----------|------|-------|
| Answer accuracy (in-domain) | | | Should be similar |
| Answer accuracy (out-of-domain) | | | CRAG should be better |
| Hallucination rate | | | CRAG should be lower |
| Latency | | | CRAG has overhead |
| Token usage | | | CRAG uses more |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| retrieval_evaluator.py | Python | Evaluator implementation |
| crag_pipeline.py | Python | Complete CRAG pipeline |
| naive_rag.py | Python | Baseline implementation |
| evaluation.ipynb | Jupyter | Test results and analysis |
| report.md | Markdown | Comparison analysis (500+ words) |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Retrieval Evaluator | 30 | Accurate quality assessment |
| Corrective Actions | 35 | All three handlers work correctly |
| Evaluation Suite | 20 | Comprehensive testing |
| Analysis Quality | 15 | Meaningful comparison insights |

### Detailed Rubric

**Retrieval Evaluator (30 points)**
- 10 points: Confidence scoring is accurate
- 10 points: Action classification is correct
- 5 points: Edge cases handled
- 5 points: Code is clean and documented

**Corrective Actions (35 points)**
- 10 points: Correct handler uses relevant docs
- 15 points: Ambiguous handler refines effectively
- 10 points: Incorrect handler falls back gracefully

**Evaluation Suite (20 points)**
- 10 points: Diverse test cases
- 5 points: Metrics are meaningful
- 5 points: Comparison is fair

**Analysis (15 points)**
- 10 points: Insights are substantive
- 5 points: Limitations acknowledged

## Resources

- Yan et al. (2024). "Corrective Retrieval Augmented Generation" - arXiv:2401.15884
- Asai et al. (2023). "Self-RAG" - arXiv:2310.11511
- Gao et al. (2024). "RAPTOR" - arXiv:2401.18059
- LangChain RAG docs: https://python.langchain.com/docs/use_cases/question_answering

## Submission

- **Format**: Python files + Jupyter notebook + Markdown report
- **Filename**: `L07_exercise_[your_name]/`
- **Due**: End of Week 7

## Hints

- Start with the evaluator - get scoring right before building handlers
- Use a small test corpus (10-20 documents) for faster iteration
- Cache LLM calls during development to save API costs
- The ambiguous handler is the hardest - test it extensively
- Consider using async for web search fallback in production

## Sample Knowledge Base

```python
# Minimal knowledge base for testing
SAMPLE_DOCS = [
    {"content": "Paris is the capital of France. It is known for the Eiffel Tower.", "source": "geography"},
    {"content": "Machine learning is a subset of AI that learns from data.", "source": "tech"},
    {"content": "Photosynthesis converts sunlight into energy in plants.", "source": "biology"},
    {"content": "William Shakespeare wrote many famous plays including Romeo and Juliet.", "source": "literature"},
    {"content": "Python is a programming language used for web development and data science.", "source": "tech"},
]

class SimpleRetriever:
    """Simple keyword-based retriever for testing."""

    def __init__(self, documents: list[dict]):
        self.documents = documents

    def retrieve(self, query: str, k: int = 5) -> list[Document]:
        """Retrieve documents by keyword matching."""
        query_terms = set(query.lower().split())

        scored = []
        for doc in self.documents:
            doc_terms = set(doc["content"].lower().split())
            overlap = len(query_terms & doc_terms)
            scored.append((overlap, doc))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [SimpleDocument(d["content"], {"source": d["source"]}) for _, d in scored[:k]]

@dataclass
class SimpleDocument:
    content: str
    metadata: dict
```

## Time Estimate
- Minimum: 5 hours
- Expected: 8 hours
- Maximum: 12 hours
