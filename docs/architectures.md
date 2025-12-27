---
layout: default
title: Architectures
nav_order: 22
mermaid: true
---

# Agent Architectures

Interactive diagrams illustrating key agent architectures covered in the course.

## Week 1: ReAct Loop

The fundamental reasoning-acting cycle.

```mermaid
flowchart TB
    subgraph ReAct["ReAct Agent Loop"]
        Q[Query] --> T[Thought]
        T --> A[Action]
        A --> O[Observation]
        O --> T
        T --> R[Response]
    end

    style T fill:#3333B2,color:white
    style A fill:#0066CC,color:white
    style O fill:#FF7F0E,color:white
```

**Key Components:**
- **Thought**: Internal reasoning about the task
- **Action**: Tool call or external interaction
- **Observation**: Result from the action
- **Loop**: Continue until task is complete

---

## Week 2: Prompting Strategies

Comparison of prompting approaches.

```mermaid
flowchart LR
    subgraph Strategies["Prompting Strategies"]
        ZS[Zero-Shot] --> Q1[Question]
        FS[Few-Shot] --> E[Examples] --> Q2[Question]
        COT[Chain-of-Thought] --> E2[Examples] --> R[Reasoning] --> Q3[Question]
    end

    Q1 --> A1[Answer]
    Q2 --> A2[Answer]
    Q3 --> A3[Better Answer]

    style COT fill:#2CA02C,color:white
    style A3 fill:#2CA02C,color:white
```

---

## Week 3: Tool Use Architecture

How agents integrate with external tools.

```mermaid
flowchart TB
    subgraph Agent["LLM Agent"]
        LLM[Language Model]
        Parser[Output Parser]
        Router[Tool Router]
    end

    subgraph Tools["Available Tools"]
        T1[Search]
        T2[Calculator]
        T3[Code Exec]
        T4[Database]
    end

    User[User Query] --> LLM
    LLM --> Parser
    Parser --> Router
    Router --> T1 & T2 & T3 & T4
    T1 & T2 & T3 & T4 --> LLM
    LLM --> Response[Response]

    style Agent fill:#f0f0ff
    style Tools fill:#fff0f0
```

---

## Week 4: Planning Architecture

Hierarchical task decomposition.

```mermaid
flowchart TB
    subgraph Planning["Planning Agent"]
        Goal[Goal] --> Decompose[Decompose]
        Decompose --> S1[Subtask 1]
        Decompose --> S2[Subtask 2]
        Decompose --> S3[Subtask 3]

        S1 --> E1[Execute]
        S2 --> E2[Execute]
        S3 --> E3[Execute]

        E1 & E2 & E3 --> Reflect[Reflect]
        Reflect -->|Revise| Decompose
        Reflect --> Complete[Complete]
    end

    style Goal fill:#3333B2,color:white
    style Reflect fill:#FF7F0E,color:white
```

---

## Week 5: Multi-Agent Orchestration

Patterns for agent coordination.

```mermaid
flowchart TB
    subgraph Hierarchical["Hierarchical Pattern"]
        O[Orchestrator] --> A1[Agent 1]
        O --> A2[Agent 2]
        O --> A3[Agent 3]
    end

    subgraph Peer["Peer-to-Peer Pattern"]
        P1[Agent] <--> P2[Agent]
        P2 <--> P3[Agent]
        P3 <--> P1
    end

    subgraph Pipeline["Pipeline Pattern"]
        L1[Agent 1] --> L2[Agent 2] --> L3[Agent 3]
    end

    style O fill:#3333B2,color:white
```

---

## Week 7: RAG Pipeline

Retrieval-Augmented Generation flow.

```mermaid
flowchart LR
    subgraph RAG["RAG Pipeline"]
        Q[Query] --> Embed[Embed Query]
        Embed --> Search[Vector Search]

        subgraph VectorDB["Vector Store"]
            D1[Doc 1]
            D2[Doc 2]
            D3[Doc 3]
        end

        Search --> VectorDB
        VectorDB --> Rank[Rerank]
        Rank --> Context[Top-K Context]
        Context --> LLM[LLM + Query]
        LLM --> Answer[Answer]
    end

    style Embed fill:#0066CC,color:white
    style LLM fill:#3333B2,color:white
```

---

## Week 8: GraphRAG

Knowledge graph enhanced retrieval.

```mermaid
flowchart TB
    subgraph GraphRAG["GraphRAG Architecture"]
        Docs[Documents] --> Extract[Entity Extraction]
        Extract --> KG[Knowledge Graph]

        Query[Query] --> Identify[Identify Entities]
        Identify --> Traverse[Graph Traversal]

        KG --> Traverse
        Traverse --> Communities[Community Detection]
        Communities --> Summarize[Hierarchical Summaries]
        Summarize --> Answer[Answer]
    end

    style KG fill:#2CA02C,color:white
```

---

## Week 9: Chain-of-Verification

Hallucination prevention through verification.

```mermaid
flowchart TB
    subgraph CoV["Chain-of-Verification"]
        Query[Query] --> Generate[Generate Draft]
        Generate --> Decompose[Decompose Claims]
        Decompose --> C1[Claim 1]
        Decompose --> C2[Claim 2]
        Decompose --> C3[Claim 3]

        C1 --> V1[Verify]
        C2 --> V2[Verify]
        C3 --> V3[Verify]

        V1 & V2 & V3 --> Revise[Revise Response]
        Revise --> Final[Verified Answer]
    end

    style Decompose fill:#FF7F0E,color:white
    style Revise fill:#2CA02C,color:white
```

---

## Framework Comparison

```mermaid
flowchart TB
    subgraph LangGraph["LangGraph"]
        LG_S[State] --> LG_N[Nodes]
        LG_N --> LG_E[Edges]
        LG_E --> LG_C[Checkpoints]
    end

    subgraph CrewAI["CrewAI"]
        CR_A[Agents] --> CR_T[Tasks]
        CR_T --> CR_P[Process]
        CR_P --> CR_R[Results]
    end

    subgraph AutoGen["AutoGen"]
        AG_A[Agents] --> AG_C[Conversation]
        AG_C --> AG_M[Messages]
        AG_M --> AG_A
    end

    style LG_S fill:#3333B2,color:white
    style CR_A fill:#0066CC,color:white
    style AG_C fill:#FF7F0E,color:white
```

---

## Using These Diagrams

### In Your Slides

Reference these diagrams in presentations by linking to this page or recreating in LaTeX with TikZ.

### In Notebooks

Use Mermaid in Jupyter with:

```python
from IPython.display import display, HTML

mermaid_code = """
graph LR
    A --> B
"""

display(HTML(f'<pre class="mermaid">{mermaid_code}</pre>'))
```

### Customization

Edit diagrams by modifying the Mermaid code. See [Mermaid documentation](https://mermaid.js.org/syntax/flowchart.html) for syntax.

---

*Diagrams are interactive - hover for details, click to zoom where supported.*
