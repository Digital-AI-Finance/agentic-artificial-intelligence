# Reading Guide: Toolformer and Tool Use

**Week 3 - Tool Use and Function Calling**

## Paper Details

- **Title**: Toolformer: Language Models Can Teach Themselves to Use Tools
- **Authors**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Year**: 2023
- **Venue**: NeurIPS 2023
- **arXiv**: https://arxiv.org/abs/2302.04761
- **Code**: https://github.com/lucidrains/toolformer-pytorch

## Paper Classification

- **Type**: Foundational (introduces self-supervised tool learning)
- **Impact**: 1500+ citations, influenced function calling in GPT-4, Claude
- **Prerequisites**: Understanding of LLM fine-tuning, perplexity

## Why This Paper Matters

Toolformer demonstrates that LLMs can learn to use external tools autonomously through self-supervised learning, without explicit human annotation of when to use tools. This paper laid the foundation for modern function calling capabilities in commercial LLMs and showed that tools can extend LLM capabilities beyond their training data.

---

## Critical Reading Guide

### Before Reading

Answer these questions to prime your reading:

1. **Problem Context**: What are the fundamental limitations of LLMs?
   - Cannot perform accurate arithmetic
   - Knowledge is frozen at training time
   - Cannot access real-time information
   - Cannot verify their own outputs

2. **Prior Work**: How did earlier systems enable LLM tool use?
   - Manual prompting with tool descriptions
   - Explicit fine-tuning on tool use examples
   - Retrieval-augmented approaches

3. **Your Hypothesis**: How might an LLM learn when to use tools vs answer directly?

### During Reading

Focus on these aspects:

#### Section 1-2: Introduction and Related Work
- [ ] What is the key insight that motivates Toolformer?
- [ ] How does self-supervised tool learning differ from supervised approaches?
- [ ] What prior work on augmented LMs does this build on?

**Key Insight**: Let the LLM decide when tools would help, then filter by whether tool use actually improves predictions.

#### Section 3: Toolformer Method

**API Call Format**:
```
text before [API_NAME(arguments) -> result] text after
```

**The Self-Supervised Pipeline**:
1. **Sampling**: Generate potential API calls given text
2. **Execution**: Run the API calls to get results
3. **Filtering**: Keep only calls that reduce perplexity
4. **Fine-tuning**: Train on successful tool uses

- [ ] How does the model know where to insert API calls?
- [ ] What is the filtering criterion (perplexity reduction)?
- [ ] How is the fine-tuning dataset constructed?

**Key Figure**: Figure 2 shows the sampling and filtering process
- Note how many samples are generated vs kept
- Understand the perplexity filtering threshold

#### Section 4: Tools and Implementation
- [ ] What tools are evaluated?
  - Calculator (QA-based arithmetic)
  - Q&A system (factual lookup)
  - Wikipedia search (current events)
  - Machine translation
  - Calendar (date/time)
- [ ] How is each tool's API designed?
- [ ] What are the design principles for tool APIs?

**Tool Design Principles** (implicit in paper):
| Principle | Example |
|-----------|---------|
| Clear input/output | Calculator: "234 + 567" -> "801" |
| Atomic operations | One calculation per call |
| Deterministic | Same input always same output |
| Text-based I/O | Easy for LLM to generate and parse |

#### Section 5: Experiments
- [ ] How is tool use evaluated?
- [ ] What baselines are compared?
- [ ] On which tasks does Toolformer improve most?

**Key Results**:
- LAMA (factual): Toolformer significantly outperforms base LLM
- Math: Calculator tool dramatically improves accuracy
- Temporal: Wikipedia search helps with recent events

#### Section 6: Analysis
- [ ] What determines when the model uses tools?
- [ ] How often does the model use tools incorrectly?
- [ ] What are the failure modes?

### After Reading

Reflect on these questions:

1. **Limitations Acknowledged**
   - What limitations do the authors mention?
   - Limited to text-in, text-out tools
   - Requires perplexity as supervision signal
   - Tools must be callable during training

2. **Unacknowledged Limitations**
   - What limitations are NOT discussed?
   - Scaling to many tools (tool selection problem)
   - Error propagation from wrong tool outputs
   - Security implications of autonomous tool use
   - Cost of API calls during training

3. **Connection to Course**
   - How does Toolformer relate to agent tool use?
   - Foundation for function calling in GPT-4, Claude
   - Shows tools can extend LLM capabilities
   - Self-supervised learning reduces annotation burden

4. **Follow-up Work**
   - What papers built on Toolformer?
   - ToolLLM: Scales to 16,000+ APIs
   - Gorilla: Retrieval-augmented tool selection
   - API-Bank: Comprehensive tool use benchmark

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - Why use perplexity reduction as the criterion for useful tool use?
   - Is self-supervised tool learning better than explicit annotation?

2. **Technical**
   - How would you extend this to tools with side effects (e.g., send email)?
   - What happens when tool APIs change after training?

3. **Practical**
   - How do commercial LLMs (GPT-4, Claude) implement tool use?
   - What's different about prompting-based vs fine-tuning-based tool use?

4. **Critical**
   - Can this approach scale to thousands of tools?
   - What are the safety implications of autonomous tool selection?

---

## Key Takeaways to Remember

1. **The Toolformer Formula**:
   ```
   Sample tool calls -> Execute -> Filter by perplexity -> Fine-tune
   ```

2. **Key Insight**: LLMs can learn when to use tools by measuring whether tool use improves their predictions.

3. **Tool API Design**: Tools should have:
   - Clear text-based inputs and outputs
   - Atomic, single-purpose operations
   - Deterministic behavior
   - Helpful error messages

4. **When Tools Help**:
   - Arithmetic and math (calculator)
   - Current information (search)
   - Factual lookup (Q&A, Wikipedia)
   - Domain-specific operations

5. **Limitations**:
   - Cannot handle multi-step tool chains
   - No reasoning about tool selection
   - Limited to tools available during training

---

## Supplementary Readings

| Paper | Relationship |
|-------|--------------|
| Gorilla (Patil et al., 2023) | Retrieval-augmented API selection |
| ToolLLM (Qin et al., 2024) | Scales to 16,000+ real-world APIs |
| API-Bank (Li et al., 2023) | Benchmark for tool use evaluation |
| ReAct (Yao et al., 2023) | Combines reasoning with tool actions |
| ToolBench (Xu et al., 2023) | Large-scale tool use benchmark |

---

## Comparison: Tool Use Approaches

| Approach | Pros | Cons |
|----------|------|------|
| Prompting (in-context) | No training, flexible | Token-limited, inconsistent |
| Fine-tuning (Toolformer) | Learned when to use | Expensive, static tools |
| Retrieval-augmented | Scales to many tools | Selection accuracy |
| Function calling (GPT-4) | Structured, reliable | Proprietary |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read the full paper (focus on Sections 3-5)
- [ ] Studied Figure 2 (the filtering pipeline)
- [ ] Understood the perplexity filtering criterion
- [ ] Compared to modern function calling (GPT-4, Claude)
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to ReAct and agent architectures

## Notes Template

Use this template for your reading notes:

```markdown
## Toolformer Reading Notes

**Date**: [your date]

### Main Contribution
[1-2 sentences on self-supervised tool learning]

### Key Method
[Describe the sample-execute-filter-finetune pipeline]

### Results Summary
[Key improvements on math, factual QA, etc.]

### Strengths
- [Strength 1]
- [Strength 2]

### Weaknesses
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Agent Design
[How does Toolformer inform agent tool use?]
```

## Practical Exercise

Design a tool API for these scenarios:

1. **Stock Price Lookup**
   ```
   Input format: ?
   Output format: ?
   Example: ?
   ```

2. **Weather Forecast**
   ```
   Input format: ?
   Output format: ?
   Example: ?
   ```

Consider: What makes a good tool API for LLM use?
