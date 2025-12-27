# Week 7 Exercise: Building a CRAG System

## Learning Objectives
- **Apply**: Implement corrective retrieval-augmented generation
- **Analyze**: Evaluate retrieval quality with confidence scoring
- **Evaluate**: Design fallback strategies for poor retrieval

## Problem Statement

Implement a Corrective RAG (CRAG) system that evaluates retrieval quality and takes corrective actions.

### Requirements

#### Part 1: Retrieval Evaluator (35 points)

Implement a lightweight evaluator that scores retrieval quality:

```python
class RetrievalEvaluator:
    def evaluate(self, query: str, documents: List[Document]) -> EvaluationResult:
        """
        Evaluate retrieval quality.

        Returns:
            EvaluationResult with:
            - action: "correct" | "ambiguous" | "incorrect"
            - confidence: float 0.0-1.0
            - reasoning: str
        """
        pass
```

Scoring thresholds:
- Correct: confidence > 0.7
- Ambiguous: 0.3 <= confidence <= 0.7
- Incorrect: confidence < 0.3

#### Part 2: Corrective Actions (35 points)

Implement handlers for each evaluation outcome:

```python
class CRAGPipeline:
    def handle_correct(self, query: str, docs: List[Document]) -> str:
        """Use documents directly for generation."""
        pass

    def handle_ambiguous(self, query: str, docs: List[Document]) -> str:
        """Refine query and re-retrieve."""
        pass

    def handle_incorrect(self, query: str, docs: List[Document]) -> str:
        """Fall back to web search (simulated)."""
        pass
```

#### Part 3: Evaluation (30 points)

Create a test suite with 10 queries spanning:
- High-quality retrieval cases
- Ambiguous retrieval cases
- Poor retrieval cases (out-of-domain)

Measure:
- Accuracy improvement over naive RAG
- Latency overhead
- Action distribution (correct/ambiguous/incorrect)

## Deliverables

1. `crag_pipeline.py` - Complete CRAG implementation
2. `evaluator.py` - Retrieval quality evaluator
3. `evaluation.ipynb` - Test results and analysis
4. `report.md` - Analysis of CRAG vs naive RAG

## Evaluation Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Evaluator accuracy | 20 | Correctly classifies retrieval quality |
| Action handlers | 20 | Proper implementation of all three actions |
| Query refinement | 15 | Effective query rewriting for ambiguous cases |
| Web fallback | 10 | Reasonable fallback strategy |
| Evaluation depth | 20 | Comprehensive testing and analysis |
| Code quality | 15 | Clean, documented, error handling |

## Time Estimate
- Minimum: 4 hours
- Expected: 6 hours
- Maximum: 10 hours
