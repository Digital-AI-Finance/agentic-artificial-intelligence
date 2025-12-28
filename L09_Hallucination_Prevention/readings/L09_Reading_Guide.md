# Week 9 Reading Guide: Hallucination Detection and Prevention

## Primary Reading

### Chain-of-Verification Reduces Hallucination in Large Language Models
**Authors**: Dhuliawala, S., Komeili, M., Xu, J., et al.
**Year**: 2023
**arXiv**: 2309.11495

#### Key Concepts
- Four-step verification pipeline
- Independent question answering
- Self-consistency checking
- Iterative refinement

#### Critical Reading Questions
1. Why is independent verification more reliable than self-correction?
2. What types of hallucinations does CoVe handle well vs. poorly?
3. How does the verification overhead compare to the accuracy gains?

---

## Secondary Readings

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation
**Authors**: Min, S., Krishna, K., Lyu, X., et al.
**Year**: 2023
**arXiv**: 2305.14251

#### Focus Areas
- Atomic fact decomposition methodology
- Scoring against knowledge sources
- Correlation with human judgments

### Survey of Hallucination in Natural Language Generation
**Authors**: Ji, Z., Lee, N., Frieske, R., et al.
**Year**: 2023
**arXiv**: 2202.03629

#### Focus Areas
- Taxonomy of hallucination types (intrinsic vs. extrinsic)
- Causes: data, training, decoding
- Mitigation strategies overview

### Self-Refine: Iterative Refinement with Self-Feedback
**Authors**: Madaan, A., Tandon, N., Gupta, P., et al.
**Year**: 2023
**arXiv**: 2303.17651

#### Focus Areas
- Iterative self-improvement loop
- Feedback generation strategies
- Stopping criteria

---

## Discussion Questions

### For Seminar
1. **Taxonomy**: How would you categorize different hallucination types for an agent context? Which are most dangerous?

2. **Detection vs. Prevention**: Is it better to prevent hallucinations at generation time or detect/correct them afterward?

3. **Knowledge Grounding**: What knowledge sources are appropriate for different domains? How do you handle conflicting sources?

4. **Confidence Calibration**: How can agents better express uncertainty when they might be hallucinating?

5. **Agent-Specific Challenges**: What unique hallucination risks do agents face (tool calls, action sequences, state tracking)?

---

## Practical Exercises

### Before Class
1. Read CoVe paper completely (focus on methodology and results)
2. Read FActScore Sections 1-3
3. Identify one example of LLM hallucination you've encountered

### After Class
1. Implement claim decomposition on a sample text
2. Test verification on known true/false claims
3. Measure your system's precision and recall

---

## Hallucination Types Reference

| Type | Example | Detection Approach |
|------|---------|-------------------|
| Factual | Wrong dates, names | External knowledge lookup |
| Logical | Invalid reasoning | Consistency checking |
| Contextual | Contradiction with input | Self-consistency |
| Temporal | Outdated information | Timestamp verification |
| Fabricated | Made-up citations | Source verification |

---

## Related Papers

| Paper | Relationship | Notes |
|-------|--------------|-------|
| TruthfulQA (Lin et al., 2022) | Benchmark | Truthfulness evaluation |
| RARR (Gao et al., 2023) | Method | Retrieve and revise |
| FactKB (Yin et al., 2023) | Resources | Knowledge base for facts |
| FLEEK (Bayat et al., 2024) | Detection | Factual error detection |

---

## Key Takeaways
1. Hallucinations have multiple causes requiring different solutions
2. Decomposition into atomic claims enables fine-grained checking
3. Independent verification outperforms self-correction
4. Perfect hallucination prevention remains unsolved
5. Agents need robust uncertainty quantification
