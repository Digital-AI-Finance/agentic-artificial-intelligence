# Week 9 Exercise: Building a Fact-Checking Agent

## Objective
Build a comprehensive fact-checking agent using Chain-of-Verification (CoVe) methodology to detect and prevent hallucinations in LLM outputs.

## Learning Outcomes
- Implement claim decomposition for atomic fact extraction
- Design verification question generation
- Build independent verification pipelines
- Create confidence calibration mechanisms

## Task Description

### Part 1: Claim Decomposition (25%)
Implement a claim extraction system that:
1. Decomposes text into atomic, verifiable claims
2. Classifies claims by type (factual, opinion, temporal, quantitative)
3. Identifies claims requiring external verification
4. Links claims to source sentences

### Part 2: Verification Question Generation (25%)
Build a question generator that:
1. Creates 2-3 verification questions per claim
2. Generates questions that are independent of the original claim
3. Targets different aspects (who, what, when, where)
4. Avoids leading questions that bias answers

### Part 3: Independent Verification (30%)
Implement the verification pipeline:
1. Answer verification questions without seeing original claim
2. Cross-reference answers with claim content
3. Calculate consistency scores
4. Handle conflicting evidence

### Part 4: Confidence Calibration (20%)
Build a confidence system that:
1. Aggregates claim-level scores to document-level
2. Flags claims below confidence threshold
3. Provides evidence for each verification decision
4. Generates corrected text for false claims

## Deliverables
1. `fact_checker.py` - Complete CoVe implementation
2. `test_cases.json` - 20+ test cases with ground truth
3. `evaluation_report.md` - Precision/recall analysis
4. `demo.ipynb` - Interactive fact-checking demo

## Test Cases Required
Include test cases for:
- Historical facts (verifiable dates, events)
- Scientific claims (quantitative data)
- Geographic information
- Biographical data
- Recent events (post-knowledge-cutoff)

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Claim Decomposition | 20 | Atomic, complete extraction |
| Question Quality | 20 | Independent, targeted questions |
| Verification Logic | 25 | Sound reasoning and scoring |
| Confidence Calibration | 20 | Well-calibrated uncertainty |
| Test Coverage | 15 | Diverse, challenging cases |

## Resources
- Chain-of-Verification (Dhuliawala et al., 2023)
- FActScore (Min et al., 2023)
- Self-Refine (Madaan et al., 2023)

## Time Estimate
- Minimum: 4 hours
- Expected: 6 hours
- Maximum: 10 hours
