# Exercise L09: Building a Fact-Checking Agent

**Week 9 - Hallucination Prevention**

## Overview

Build a comprehensive fact-checking agent using Chain-of-Verification (CoVe) methodology to detect and prevent hallucinations in LLM outputs.

## Learning Objectives

- **Primary (Apply)**: Implement claim decomposition for atomic fact extraction
- **Secondary (Analyze)**: Evaluate verification strategies and their effectiveness
- **Tertiary (Create)**: Design a multi-layer hallucination prevention pipeline

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Understanding of RAG and retrieval systems

## Problem Statement

LLMs hallucinate - they generate plausible but false information. For agent systems, this is critical: an agent acting on false information can cause real harm. The Chain-of-Verification (CoVe) approach reduces hallucinations by independently verifying generated content.

### Task 1: Claim Decomposition (25 points)

Implement a claim extraction system that breaks text into atomic, verifiable claims.

**Requirements:**
1. Decompose text into atomic claims (single verifiable statements)
2. Classify claims by type: factual, opinion, temporal, quantitative
3. Identify which claims require external verification
4. Link each claim back to its source sentence

**Test Input:**
```
Albert Einstein was born in Ulm, Germany in 1879. He developed the theory
of relativity and won the Nobel Prize in Physics in 1921 for his explanation
of the photoelectric effect. He is widely considered the most influential
physicist of the 20th century.
```

**Expected Output:**
```json
{
  "claims": [
    {"text": "Einstein was born in Ulm, Germany", "type": "factual", "verifiable": true},
    {"text": "Einstein was born in 1879", "type": "temporal", "verifiable": true},
    {"text": "Einstein developed the theory of relativity", "type": "factual", "verifiable": true},
    {"text": "Einstein won the Nobel Prize in Physics in 1921", "type": "temporal", "verifiable": true},
    {"text": "The Nobel Prize was for the photoelectric effect", "type": "factual", "verifiable": true},
    {"text": "Einstein is the most influential physicist of the 20th century", "type": "opinion", "verifiable": false}
  ]
}
```

### Task 2: Verification Question Generation (25 points)

Build a question generator that creates independent verification questions.

**Requirements:**
1. Create 2-3 verification questions per claim
2. Questions must be answerable independently (no reference to original claim)
3. Target different aspects (who, what, when, where, how much)
4. Avoid leading questions that bias answers

**Example:**

Claim: "Einstein won the Nobel Prize in Physics in 1921"

**Good questions:**
- "In what year did Albert Einstein receive the Nobel Prize?"
- "What field was Albert Einstein's Nobel Prize in?"
- "Who won the Nobel Prize in Physics in 1921?"

**Bad questions (leading):**
- "Did Einstein win the Nobel Prize in 1921?" (yes/no leads to confirmation)
- "Einstein won the Nobel Prize, didn't he?" (assumes the claim is true)

### Task 3: Independent Verification Pipeline (30 points)

Implement the full CoVe verification pipeline:

**Pipeline Steps:**
1. Generate baseline response to a query
2. Extract and decompose claims from response
3. Generate verification questions for each claim
4. Answer verification questions independently (fresh context)
5. Cross-reference verification answers with original claims
6. Calculate consistency scores
7. Generate final verified response

**Key Implementation Detail:**
The verification step MUST be independent. Do not include the original response in the verification prompt. This prevents the model from rationalizing its own errors.

**Scoring Function:**
```python
def consistency_score(claim, verification_answer):
    """
    Returns score 0-1 based on how well verification supports claim.
    1.0 = fully supported
    0.5 = partially supported / ambiguous
    0.0 = contradicted
    """
    # Implement using LLM comparison or semantic similarity
    pass
```

### Task 4: Confidence Calibration and FActScore (20 points)

Implement FActScore-style atomic fact evaluation:

**Requirements:**
1. Calculate document-level factuality score from claim scores
2. Flag claims below confidence threshold (e.g., < 0.7)
3. Provide evidence for each verification decision
4. Generate corrected text for claims marked as false

**FActScore Formula:**
```
FActScore = (Number of supported atomic facts) / (Total atomic facts)
```

**Output Format:**
```json
{
  "original_text": "...",
  "factscore": 0.85,
  "claims": [
    {"claim": "...", "score": 0.95, "status": "verified", "evidence": "..."},
    {"claim": "...", "score": 0.3, "status": "flagged", "correction": "..."}
  ],
  "corrected_text": "..."
}
```

## Test Cases Required

Include at least 20 test cases covering:

| Category | Count | Examples |
|----------|-------|----------|
| Historical facts | 5 | Dates of events, people's birth/death |
| Scientific claims | 5 | Physical constants, chemical properties |
| Geographic information | 3 | Capitals, populations, locations |
| Biographical data | 4 | Awards, education, positions held |
| Recent events | 3 | Post-knowledge-cutoff (expect flagging) |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| fact_checker.py | Python | Complete CoVe implementation |
| test_cases.json | JSON | 20+ test cases with ground truth |
| evaluation_report.md | Markdown | Precision/recall analysis |
| demo.ipynb | Jupyter | Interactive fact-checking demo |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Claim Decomposition | 20 | Atomic, complete extraction |
| Question Quality | 20 | Independent, targeted questions |
| Verification Logic | 25 | Sound reasoning and scoring |
| Confidence Calibration | 20 | Well-calibrated uncertainty |
| Test Coverage | 15 | Diverse, challenging cases |

### Detailed Rubric

**Claim Decomposition (20 points)**
- 10 points: Claims are truly atomic (single fact each)
- 5 points: Classification is accurate
- 5 points: Source linking is correct

**Question Quality (20 points)**
- 10 points: Questions are genuinely independent
- 5 points: Questions cover multiple aspects
- 5 points: No leading questions

**Verification Logic (25 points)**
- 15 points: Independent verification implemented correctly
- 5 points: Consistency scoring is reasonable
- 5 points: Conflicting evidence handled

**Confidence Calibration (20 points)**
- 10 points: FActScore correctly calculated
- 5 points: Flagging threshold appropriate
- 5 points: Corrections are accurate

**Test Coverage (15 points)**
- 10 points: Diverse test cases
- 5 points: Includes challenging edge cases

## Resources

- Dhuliawala et al. (2023). "Chain-of-Verification" - arXiv:2309.11495
- Min et al. (2023). "FActScore" - arXiv:2305.14251
- Madaan et al. (2023). "Self-Refine" - arXiv:2303.17651

## Submission

- **Format**: Python files + Jupyter notebook + Markdown report
- **Filename**: `L09_exercise_[your_name]/`
- **Due**: End of Week 9

## Hints

- Start with simple claims before handling complex multi-part statements
- Use different prompts for decomposition vs verification
- Consider using retrieval (Wikipedia API) for ground truth
- Pay attention to temporal claims - verify exact dates

## Sample Implementation Skeleton

```python
class FactChecker:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.threshold = 0.7

    def decompose_claims(self, text: str) -> list[dict]:
        """Extract atomic claims from text."""
        pass

    def generate_questions(self, claim: dict) -> list[str]:
        """Generate verification questions for a claim."""
        pass

    def verify_independently(self, questions: list[str]) -> list[str]:
        """Answer questions without access to original claim."""
        pass

    def calculate_consistency(self, claim: dict, answers: list[str]) -> float:
        """Score how well answers support the claim."""
        pass

    def full_verification(self, text: str) -> dict:
        """Run complete CoVe pipeline on text."""
        pass
```

## Time Estimate
- Minimum: 4 hours
- Expected: 6 hours
- Maximum: 10 hours
