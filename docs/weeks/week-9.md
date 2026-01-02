---
layout: week
title: "Week 9: Hallucination Prevention"
week_number: 9
nav_order: 9
parent: Weeks
---

## Key Concepts

**Hallucination**: LLM generates plausible but factually incorrect content. Not random errors - often confidently stated and internally consistent.

**Hallucination Types**:
- **Factual**: Fabricated facts, non-existent entities, wrong relationships
- **Faithfulness**: Contradicts provided context or source documents
- **Instruction**: Ignores or misinterprets user instructions

**Chain-of-Verification (CoVe)**: Generate initial response, plan verification questions, answer independently, then produce verified response.

**FActScore**: Fine-grained atomic evaluation - fraction of atomic facts supported by a knowledge source.

## Exercise

Build a fact-checking agent using Chain-of-Verification:
1. Decompose claims into atomic facts (single verifiable statements)
2. Generate verification questions for each claim
3. Answer verification questions independently (without seeing original response)
4. Check consistency between verification answers and original claims
5. Generate a corrected response based on verification results

## Discussion Questions

1. What types of hallucinations are hardest to detect? Why?
2. How should agents express uncertainty without becoming overly cautious?
3. Can verification be done efficiently at scale, or is it too costly?
4. Why is independent verification more effective than self-correction?
5. How do you balance the latency cost of verification against accuracy gains?

## Additional Resources

- [FActScore GitHub](https://github.com/shmsw25/FActScore)
- [Hallucination Survey](https://arxiv.org/abs/2202.03629)
- [SelfCheckGPT](https://arxiv.org/abs/2303.08896)
