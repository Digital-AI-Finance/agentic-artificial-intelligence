---
layout: week
title: "Week 11: Domain Applications"
week_number: 11
nav_order: 11
parent: Weeks
---

## Key Concepts

**Domain Maturity Landscape**:
- **Code (High)**: Clear success criteria (tests pass), sandboxed execution, active deployment
- **Finance (Medium)**: Regulatory constraints, compliance requirements, emerging deployments
- **Healthcare (Emerging)**: High stakes, human oversight required, FDA/HIPAA compliance

**Flow Engineering**: AlphaCodium's structured multi-stage pipeline approach - break complex tasks into stages, generate and run tests iteratively.

**SWE-bench Performance**: Best agents solve ~50% of real GitHub issues - significant but still far from human-level.

**Cross-Domain Patterns**: Verification intensity should match domain risk level.

## Exercise

Build a domain-specific agent for one of:
1. **Code Generation**: Flow engineering approach with test-driven iteration
2. **Research Assistant**: Literature search with citation verification
3. **Financial Analysis**: Market data analysis with compliance guardrails
4. **Clinical Decision Support**: Evidence-based recommendations with human oversight

## Discussion Questions

1. How do domain constraints affect agent architecture design?
2. What safety measures are essential for high-stakes domains like healthcare?
3. When should agents defer to humans vs act autonomously?
4. How does regulatory compliance (SEC, FDA, HIPAA) constrain agent capabilities?
5. What is the appropriate verification intensity for each domain?

## Additional Resources

- [Devin](https://www.cognition-labs.com/introducing-devin)
- [AlphaCodium](https://github.com/Codium-ai/AlphaCodium)
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent)
- [Cursor AI](https://cursor.sh/)
