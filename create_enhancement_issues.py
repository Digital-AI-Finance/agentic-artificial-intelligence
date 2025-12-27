"""
Create 58 GitHub issues for world-leading GitHub Pages enhancement.
Run with: python create_enhancement_issues.py
"""

import subprocess
import time

REPO = "Digital-AI-Finance/agentic-artificial-intelligence"

# Milestone titles (gh CLI needs titles, not numbers)
MILESTONES = {
    "M1": "M1: Content Exposure",
    "M2": "M2: Quiz Completion",
    "M3": "M3: Quality Assurance",
    "M4": "M4: Interactive Features",
    "M5": "M5: User Experience",
    "M6": "M6: Technical Infrastructure",
    "M7": "M7: Community Features",
    "M8": "M8: Accessibility",
}

# All 58 issues organized by milestone
ISSUES = [
    # ==================== MILESTONE 1: Content Exposure (8 issues) ====================
    {
        "title": "[PAGES] Create Chart Gallery Page",
        "milestone": "M1",
        "labels": ["type:pages", "priority:critical"],
        "body": """## Overview
Create a dedicated chart gallery page at `/charts/` displaying all 48 course visualizations.

## Requirements
- Display all charts from L01-L12 folders (4 per lesson = 48 total)
- Thumbnail previews with click-to-enlarge
- Filter by week and topic
- Download links for PDF files
- Source code links to chart.py files

## Technical Details
- Location: `docs/charts.md`
- Use Jekyll's data files to list charts
- Responsive grid layout
- Lazy loading for performance

## Chart Inventory
| Week | Charts |
|------|--------|
| L01 | agent_definition, react_paradigm, agent_taxonomy, trajectory_structure |
| L02 | cot_comparison, tot_tree, self_consistency, context_window |
| ... | (continue for all 12 weeks) |

## Acceptance Criteria
- [ ] All 48 charts displayed with thumbnails
- [ ] Filtering works by week and topic
- [ ] PDFs downloadable
- [ ] Source code accessible
- [ ] Mobile responsive
"""
    },
    {
        "title": "[PAGES] Expose L01-L05 Exercises on Week Pages",
        "milestone": "M1",
        "labels": ["type:pages", "priority:critical"],
        "body": """## Overview
Add exercise sections to week pages 1-5 linking to exercise markdown files.

## Exercises to Link
| Week | Exercise File | Title |
|------|--------------|-------|
| L01 | exercises/L01_agent_classification.md | Agent Classification |
| L02 | exercises/L02_prompt_engineering.md | Prompt Engineering |
| L03 | exercises/L03_tool_design.md | Tool Design |
| L04 | exercises/L04_planning_agent.md | Planning Agent |
| L05 | exercises/L05_multi_agent_design.md | Multi-Agent Design |

## Requirements
- Add "Exercises" section to each week page
- Include rubric summary (100 points breakdown)
- Link to full exercise markdown
- Show estimated time
- Display learning objectives

## Files to Modify
- `docs/weeks/week-1.md` through `docs/weeks/week-5.md`
- `docs/_layouts/week.html` (add exercise section template)
"""
    },
    {
        "title": "[PAGES] Expose L06-L12 Exercises on Week Pages",
        "milestone": "M1",
        "labels": ["type:pages", "priority:critical"],
        "body": """## Overview
Add exercise sections to week pages 6-12 with consistent formatting.

## Exercises to Link
| Week | Exercise File | Title |
|------|--------------|-------|
| L06 | L06_Exercise.md | Framework Implementation |
| L07 | L07_Exercise.md | RAG Pipeline |
| L08 | L08_Exercise.md | GraphRAG |
| L09 | L09_Exercise.md | Verification Pipeline |
| L10 | L10_Exercise.md | Agent Evaluation |
| L11 | L11_Exercise.md | Domain Agent |
| L12 | L12_Exercise.md | Research Proposal |

## Requirements
- Consistent formatting with weeks 1-5
- Include rubric and time estimates
- Add submission guidelines

## Files to Modify
- `docs/weeks/week-6.md` through `docs/weeks/week-12.md`
"""
    },
    {
        "title": "[PAGES] Expose L01-L06 Reading Guides",
        "milestone": "M1",
        "labels": ["type:pages", "priority:critical"],
        "body": """## Overview
Add reading guide sections with paper links and arXiv badges to weeks 1-6.

## Reading Guides to Link
| Week | File | Paper |
|------|------|-------|
| L01 | readings/L01_react_reading_guide.md | ReAct (Yao et al., 2023) |
| L02 | readings/L02_cot_reading_guide.md | Chain-of-Thought (Wei et al., 2022) |
| L03 | readings/L03_toolformer_reading_guide.md | Toolformer (Schick et al., 2023) |
| L04 | readings/L04_reflexion_reading_guide.md | Reflexion (Shinn et al., 2023) |
| L05 | readings/L05_mas_survey_reading_guide.md | Multi-Agent Survey |
| L06 | L06_Reading_Guide.md | LangGraph/CrewAI |

## Requirements
- Add "Required Reading" section to week pages
- Include arXiv badge with link
- Show reading guide summary
- Add discussion questions preview
"""
    },
    {
        "title": "[PAGES] Expose L07-L12 Reading Guides",
        "milestone": "M1",
        "labels": ["type:pages", "priority:high"],
        "body": """## Overview
Add reading guide sections to weeks 7-12 with consistent formatting.

## Reading Guides
| Week | File | Paper |
|------|------|-------|
| L07 | L07_Reading_Guide.md | Self-RAG (Asai et al., 2023) |
| L08 | L08_Reading_Guide.md | GraphRAG (Edge et al., 2024) |
| L09 | L09_Reading_Guide.md | Chain-of-Verification |
| L10 | L10_Reading_Guide.md | AgentBench (Liu et al., 2023) |
| L11 | L11_Reading_Guide.md | AlphaCodium |
| L12 | L12_Reading_Guide.md | Generative Agents |

## Requirements
- Consistent with weeks 1-6 format
- Include arXiv badges and discussion questions
"""
    },
    {
        "title": "[PAGES] Remove Coming Soon Badges for L06-L12",
        "milestone": "M1",
        "labels": ["type:pages", "priority:critical"],
        "body": """## Overview
Update index page to show L06-L12 as complete - content exists but badges are incorrect.

## Current State
- Weeks 6-12 show "Coming Soon" badges
- All content is actually complete in repository:
  - L06-L12 slides exist
  - All notebooks have Colab badges
  - Exercises and readings are complete

## Changes Required
1. Update `docs/index.md` - remove conditional "Coming Soon" badges
2. Update `docs/_data/weeks.yml` - ensure status is "complete" for all weeks
3. Update any CSS hiding completed week content

## Files to Modify
- `docs/index.md`
- `docs/_data/weeks.yml`

## Acceptance Criteria
- [ ] All 12 weeks show as available
- [ ] No "Coming Soon" badges visible
- [ ] All week links are clickable
"""
    },
    {
        "title": "[PAGES] Add Colab Badges to All Notebook Links",
        "milestone": "M1",
        "labels": ["type:pages", "priority:high"],
        "body": """## Overview
Ensure every notebook reference on the website has a working "Open in Colab" badge.

## Notebooks Inventory (14 total)
| Notebook | Colab Link |
|----------|------------|
| L01_first_agent.ipynb | colab.research.google.com/github/Digital-AI-Finance/... |
| L02_prompting_strategies.ipynb | ... |
| L03_mcp_tool_implementation.ipynb | ... |
| L03_function_calling_comparison.ipynb | ... |
| L04_reflexion_implementation.ipynb | ... |
| L05_message_passing.ipynb | ... |
| L05_coordination_demo.ipynb | ... |
| L06_LangGraph_Agent.ipynb | ... |
| L07_Self_RAG.ipynb | ... |
| L08_GraphRAG.ipynb | ... |
| L09_Verification.ipynb | ... |
| L10_Benchmarking.ipynb | ... |
| L11_Code_Agent.ipynb | ... |
| L12_Generative_Agents.ipynb | ... |

## Requirements
- Badge format: `[![Open In Colab](badge_url)](colab_link)`
- Verify all links work
- Add to week pages, index, and getting-started
"""
    },
    {
        "title": "[PAGES] Create PDF Slides Download Links",
        "milestone": "M1",
        "labels": ["type:pages", "priority:high"],
        "body": """## Overview
Add direct links to compiled PDF slides for each week with file size indicators.

## Slides Inventory
| Week | File | Topic |
|------|------|-------|
| L01 | L01_Introduction_Agentic_AI.pdf | Introduction |
| L02 | L02_LLM_Foundations_Agents.pdf | LLM Foundations |
| L03 | L03_Tool_Use_Function_Calling.pdf | Tool Use |
| ... | ... | ... |

## Requirements
- Download button on each week page
- Show file size (e.g., "Download PDF (2.3 MB)")
- Direct link to GitHub raw file
- Add to resources section
"""
    },

    # ==================== MILESTONE 2: Quiz Completion (9 issues) ====================
    {
        "title": "[QUIZ] Week 4: Planning and Reasoning",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ quiz questions covering Week 4: Planning and Reasoning.

## Topics to Cover
- Reflexion framework and verbal reinforcement
- LATS (Language Agent Tree Search)
- Hierarchical planning
- Episodic memory systems
- Plan-and-Solve prompting

## Question Format
```yaml
- question: "Question text?"
  options:
    - "Option A"
    - "Option B"
    - "Option C"
    - "Option D"
  correct: 1  # 0-indexed
  explanation: "Why B is correct..."
```

## Required Questions (minimum 5)
1. Reflexion mechanism question
2. LATS tree search question
3. Planning decomposition question
4. Memory systems question
5. Self-improvement question

## File to Modify
- `docs/_data/quizzes.yml` - Add `week4:` section
"""
    },
    {
        "title": "[QUIZ] Week 6: Agent Frameworks",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ quiz questions on LangGraph, AutoGen, CrewAI frameworks.

## Topics to Cover
- LangGraph state machines and graphs
- AutoGen conversation patterns
- CrewAI role-based agents
- Framework selection criteria
- Orchestration patterns

## Required Questions (minimum 5)
1. LangGraph state management
2. AutoGen agent types
3. CrewAI task delegation
4. Framework comparison
5. When to use which framework
"""
    },
    {
        "title": "[QUIZ] Week 7: Advanced RAG",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on Self-RAG, CRAG, RAPTOR.

## Topics to Cover
- Self-RAG reflection tokens
- CRAG corrective retrieval
- RAPTOR hierarchical summarization
- Adaptive retrieval strategies
- When to retrieve decisions

## Required Questions (minimum 5)
1. Self-RAG architecture
2. CRAG correction mechanism
3. RAPTOR tree structure
4. Retrieval decision making
5. RAG strategy comparison
"""
    },
    {
        "title": "[QUIZ] Week 8: GraphRAG and Knowledge",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on knowledge graphs and GraphRAG.

## Topics to Cover
- Knowledge graph construction
- Entity and relationship extraction
- Community detection
- Multi-hop reasoning
- Graph vs. vector retrieval

## Required Questions (minimum 5)
1. Entity extraction
2. Community summarization
3. Multi-hop queries
4. Graph traversal
5. GraphRAG vs standard RAG
"""
    },
    {
        "title": "[QUIZ] Week 9: Hallucination Prevention",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on hallucination types and prevention.

## Topics to Cover
- Hallucination taxonomy (intrinsic vs extrinsic)
- Chain-of-Verification (CoVe)
- FActScore evaluation
- Claim decomposition
- Self-Refine technique

## Required Questions (minimum 5)
1. Hallucination types
2. CoVe verification steps
3. FActScore calculation
4. Claim decomposition
5. Mitigation strategies
"""
    },
    {
        "title": "[QUIZ] Week 10: Agent Evaluation",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on AgentBench, SWE-bench, GAIA.

## Topics to Cover
- AgentBench task categories
- SWE-bench code evaluation
- WebArena web navigation
- GAIA reasoning benchmark
- LLM-as-Judge methodology

## Required Questions (minimum 5)
1. AgentBench domains
2. SWE-bench metrics
3. GAIA difficulty levels
4. Evaluation metrics
5. LLM-as-Judge criteria
"""
    },
    {
        "title": "[QUIZ] Week 11: Domain Applications",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on domain-specific agents.

## Topics to Cover
- Code generation agents (AlphaCodium, Devin)
- Financial agents (regulatory constraints)
- Healthcare agents (safety requirements)
- Research assistants
- Domain adaptation strategies

## Required Questions (minimum 5)
1. Code agent architectures
2. Financial compliance
3. Healthcare safety
4. Domain tool integration
5. Specialized prompting
"""
    },
    {
        "title": "[QUIZ] Week 12: Research Frontiers",
        "milestone": "M2",
        "labels": ["type:quiz", "priority:high"],
        "body": """## Overview
Create 5+ questions on research frontiers.

## Topics to Cover
- Generative Agents (Park et al.)
- Voyager open-ended learning
- Constitutional AI safety
- Emergent behaviors
- Open research problems

## Required Questions (minimum 5)
1. Generative agent memory
2. Voyager skill library
3. Constitutional AI principles
4. Emergence in multi-agent
5. Future research directions
"""
    },
    {
        "title": "[QUIZ] Create Quiz Progress Tracker",
        "milestone": "M2",
        "labels": ["type:quiz", "type:pages", "priority:high"],
        "body": """## Overview
Build localStorage-based quiz progress tracker.

## Features
- Track completion per week
- Show overall course progress percentage
- Visual progress bars
- Reset functionality
- Persist across sessions

## Technical Implementation
- Use localStorage for persistence
- Update `_includes/quiz.html`
- Add progress dashboard to quizzes.md
- Show on index page

## UI Requirements
- Progress bar per week (0-100%)
- Overall course completion
- "Continue where you left off" link
- Clear progress button
"""
    },

    # ==================== MILESTONE 3: Quality Assurance (14 issues) ====================
    {
        "title": "[QA] Hallucination Check L01 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Overview
Verify all citations, statistics, and paper references in L01 slides.

## Verification Checklist
- [ ] ReAct paper citation (Yao et al., 2023) - arXiv:2210.03629
- [ ] Wang et al. 2024 survey - arXiv:2308.11432
- [ ] Agent definition from Russell & Norvig
- [ ] All statistics and numbers
- [ ] Framework version claims
- [ ] Benchmark numbers

## Process
1. Extract all factual claims from L01_Introduction_Agentic_AI.tex
2. Verify each claim against source
3. Document any corrections needed
4. Update slides if errors found

## Output
- Verification report with status per claim
- List of corrections made
- Last verified date
"""
    },
    {
        "title": "[QA] Hallucination Check L02 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Overview
Verify CoT, ToT paper claims in L02 slides.

## Papers to Verify
- Chain-of-Thought (Wei et al., 2022) - arXiv:2201.11903
- Tree of Thoughts (Yao et al., 2023) - arXiv:2305.10601
- Self-Consistency (Wang et al., 2023) - arXiv:2203.11171
- Zero-Shot Reasoners (Kojima et al., 2022) - arXiv:2205.11916

## Verification Items
- [ ] Accuracy improvement percentages
- [ ] Benchmark results (GSM8K, MATH)
- [ ] Method descriptions
- [ ] Author attributions
"""
    },
    {
        "title": "[QA] Hallucination Check L03 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Overview
Verify MCP, Toolformer, Gorilla claims in L03 slides.

## Papers to Verify
- Toolformer (Schick et al., 2023) - arXiv:2302.04761
- Gorilla (Patil et al., 2023) - arXiv:2305.15334
- API-Bank (Li et al., 2023) - arXiv:2304.08244

## Verification Items
- [ ] MCP protocol specifications
- [ ] API accuracy claims
- [ ] Tool use benchmarks
- [ ] Function calling syntax
"""
    },
    {
        "title": "[QA] Hallucination Check L04 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify Reflexion, LATS claims in L04.

## Papers
- Reflexion (Shinn et al., 2023) - arXiv:2303.11366
- LATS (Zhou et al., 2024) - arXiv:2310.04406

## Items to Verify
- [ ] Performance improvements
- [ ] Algorithm descriptions
- [ ] Benchmark results
"""
    },
    {
        "title": "[QA] Hallucination Check L05 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify AutoGen, MetaGPT, ChatDev claims in L05.

## Papers
- AutoGen (Wu et al., 2023) - arXiv:2308.08155
- MetaGPT (Hong et al., 2023) - arXiv:2308.00352
- ChatDev (Qian et al., 2024) - arXiv:2307.07924

## Items to Verify
- [ ] Multi-agent coordination claims
- [ ] Software generation benchmarks
- [ ] Communication protocols
"""
    },
    {
        "title": "[QA] Hallucination Check L06 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify LangGraph, CrewAI documentation claims in L06.

## Sources
- LangGraph docs: langchain-ai.github.io/langgraph
- CrewAI docs: docs.crewai.com
- TaskWeaver (Qiao et al., 2024) - arXiv:2311.17541

## Items to Verify
- [ ] API syntax accuracy
- [ ] Feature availability
- [ ] Version compatibility
"""
    },
    {
        "title": "[QA] Hallucination Check L07 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify Self-RAG, CRAG, RAPTOR claims in L07.

## Papers
- Self-RAG (Asai et al., 2023) - arXiv:2310.11511
- CRAG (Yan et al., 2024) - arXiv:2401.15884
- RAPTOR (Sarthi et al., 2024) - arXiv:2401.18059

## Items to Verify
- [ ] Retrieval accuracy numbers
- [ ] Architecture descriptions
- [ ] Benchmark comparisons
"""
    },
    {
        "title": "[QA] Hallucination Check L08 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify GraphRAG, HippoRAG claims in L08.

## Papers
- GraphRAG (Edge et al., 2024) - Microsoft Research
- Graph of Thoughts (Besta et al., 2024) - arXiv:2308.09687
- HippoRAG (Gutierrez et al., 2024) - arXiv:2405.14831

## Items to Verify
- [ ] Community detection claims
- [ ] Multi-hop accuracy
- [ ] Knowledge graph construction
"""
    },
    {
        "title": "[QA] Hallucination Check L09 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify FActScore, CoVe claims in L09.

## Papers
- FActScore (Min et al., 2023) - arXiv:2305.14251
- Chain-of-Verification (Dhuliawala et al., 2023) - arXiv:2309.11495
- Self-Refine (Madaan et al., 2023) - arXiv:2303.17651

## Items to Verify
- [ ] Hallucination statistics
- [ ] Verification effectiveness
- [ ] Benchmark results
"""
    },
    {
        "title": "[QA] Hallucination Check L10 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify AgentBench, SWE-bench numbers in L10.

## Papers
- AgentBench (Liu et al., 2023) - arXiv:2308.03688
- SWE-bench (Jimenez et al., 2024) - arXiv:2310.06770
- WebArena (Zhou et al., 2024) - arXiv:2307.13854
- GAIA (Mialon et al., 2024) - arXiv:2311.12983

## Items to Verify
- [ ] Leaderboard numbers
- [ ] Task success rates
- [ ] Model comparisons
"""
    },
    {
        "title": "[QA] Hallucination Check L11 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify Devin, AlphaCodium, FinAgent claims in L11.

## Papers
- AlphaCodium (Ridnik et al., 2024) - arXiv:2401.08500
- MDAgents (Kim et al., 2024) - arXiv:2404.15488
- FinAgent (Li et al., 2024) - arXiv:2402.18485

## Items to Verify
- [ ] Code generation benchmarks
- [ ] Domain-specific performance
- [ ] Accuracy claims
"""
    },
    {
        "title": "[QA] Hallucination Check L12 Slides",
        "milestone": "M3",
        "labels": ["type:qa", "priority:high"],
        "body": """## Verify Voyager, Generative Agents claims in L12.

## Papers
- Generative Agents (Park et al., 2023) - arXiv:2304.03442
- Voyager (Wang et al., 2023) - arXiv:2305.16291
- Constitutional AI (Bai et al., 2022) - arXiv:2212.08073

## Items to Verify
- [ ] Emergent behavior claims
- [ ] Skill acquisition metrics
- [ ] Safety evaluation results
"""
    },
    {
        "title": "[QA] Create Verification Report Page",
        "milestone": "M3",
        "labels": ["type:qa", "type:pages", "priority:high"],
        "body": """## Overview
Create a page documenting verification status of all slide content.

## Page Content
- Table of all slides with last verified date
- Status: Verified / Pending / Issues Found
- Links to arXiv papers
- Correction log

## Location
- `docs/verification.md`

## Template
| Lesson | Last Verified | Status | Issues |
|--------|--------------|--------|--------|
| L01 | 2025-01-XX | Verified | None |
| L02 | ... | ... | ... |
"""
    },
    {
        "title": "[QA] Automate Link Checking in CI",
        "milestone": "M3",
        "labels": ["type:qa", "type:infra", "priority:high"],
        "body": """## Overview
Add GitHub Action to check all external links weekly.

## Links to Check
- arXiv paper links
- DOI references
- Documentation URLs
- GitHub repository links
- Colab notebook links

## Implementation
- Use `lychee` or `linkchecker` action
- Run weekly on schedule
- Report broken links as issues
- Exclude known false positives

## File
- `.github/workflows/link-check.yml`
"""
    },

    # ==================== MILESTONE 4: Interactive Features (6 issues) ====================
    {
        "title": "[PAGES] Implement Pyodide Code Playground",
        "milestone": "M4",
        "labels": ["type:pages", "priority:medium"],
        "body": """## Overview
Add browser-based Python execution using Pyodide.

## Features
- Embed Python REPL on code snippet pages
- Pre-load: numpy, matplotlib, langchain stubs
- Timeout: 30 seconds max execution
- Reset environment button

## Technical Implementation
- Load Pyodide via CDN
- Create `_includes/pyodide-playground.html`
- Use Web Workers for non-blocking
- Cache in IndexedDB

## Example Usage
```liquid
{% include pyodide-playground.html code="print('Hello Agent!')" %}
```
"""
    },
    {
        "title": "[PAGES] Interactive Architecture Diagrams",
        "milestone": "M4",
        "labels": ["type:pages", "priority:medium"],
        "body": """## Overview
Build D3.js/Mermaid interactive diagrams with hover details.

## Diagrams to Create
1. ReAct loop (animated cycle)
2. Multi-agent communication (message passing visualization)
3. RAG pipeline (interactive flow)
4. Planning hierarchy (expandable tree)

## Features
- Hover for component details
- Click to expand sections
- Animated transitions
- Mobile-friendly touch

## Files
- `docs/assets/js/diagrams/`
- `docs/_includes/diagram.html`
"""
    },
    {
        "title": "[PAGES] Course Progress Tracking",
        "milestone": "M4",
        "labels": ["type:pages", "priority:medium"],
        "body": """## Overview
Implement localStorage-based progress tracker.

## Track Progress For
- Readings completed
- Quizzes taken
- Exercises submitted
- Notebooks run

## Dashboard Features
- Overall completion percentage
- Per-week breakdown
- Badge system for milestones
- Export/import progress

## Implementation
- localStorage with JSON structure
- Dashboard page at `/progress/`
- Widget on each week page
"""
    },
    {
        "title": "[PAGES] Interactive Comparison Tables",
        "milestone": "M4",
        "labels": ["type:pages", "priority:medium"],
        "body": """## Overview
Build sortable/filterable comparison tables.

## Tables to Create
1. Framework comparison (LangGraph vs CrewAI vs AutoGen)
2. LLM provider comparison
3. RAG strategy comparison
4. Benchmark results comparison

## Features
- Sort by any column
- Filter by criteria
- Highlight best values
- Export to CSV
"""
    },
    {
        "title": "[PAGES] Code Copy Buttons",
        "milestone": "M4",
        "labels": ["type:pages", "priority:medium"],
        "body": """## Overview
Add one-click copy functionality to all code blocks.

## Implementation
- Add copy button to all `<pre><code>` blocks
- Visual feedback on copy (checkmark)
- Works on mobile
- Accessible (keyboard support)

## Files
- `docs/assets/js/copy-code.js`
- `docs/_sass/custom.scss` (button styles)
"""
    },
    {
        "title": "[PAGES] Estimated Reading Time",
        "milestone": "M4",
        "labels": ["type:pages", "priority:low"],
        "body": """## Overview
Auto-calculate and display reading time per page.

## Calculation
- Average: 200 words per minute
- Add time for code blocks
- Add time for images/diagrams

## Display
- Show at top of each page
- Format: "5 min read"
- Include in metadata
"""
    },

    # ==================== MILESTONE 5: User Experience (7 issues) ====================
    {
        "title": "[UX] Week Page Navigation",
        "milestone": "M5",
        "labels": ["type:ux", "priority:medium"],
        "body": """## Overview
Add prev/next week buttons and progress breadcrumbs.

## Features
- Previous/Next week arrows
- Current week indicator
- Progress breadcrumb trail
- Jump to specific week dropdown

## Implementation
- Update `_layouts/week.html`
- Add navigation component
- Keyboard shortcuts (left/right arrows)
"""
    },
    {
        "title": "[UX] Keyboard Shortcuts",
        "milestone": "M5",
        "labels": ["type:ux", "priority:medium"],
        "body": """## Overview
Implement keyboard shortcuts for power users.

## Shortcuts
| Key | Action |
|-----|--------|
| Cmd/Ctrl + K | Open search |
| Left Arrow | Previous week |
| Right Arrow | Next week |
| Escape | Close modals |
| ? | Show shortcuts help |

## Implementation
- JavaScript event listeners
- Help modal with shortcut list
- Respect focus state
"""
    },
    {
        "title": "[UX] Auto Table of Contents",
        "milestone": "M5",
        "labels": ["type:ux", "priority:medium"],
        "body": """## Overview
Auto-generate floating TOC for pages with 5+ headings.

## Features
- Sticky sidebar TOC
- Highlight current section
- Smooth scroll on click
- Collapse on mobile
- Only show for long pages
"""
    },
    {
        "title": "[UX] Mobile Navigation",
        "milestone": "M5",
        "labels": ["type:ux", "priority:medium"],
        "body": """## Overview
Optimize navigation for mobile devices.

## Improvements
- Better hamburger menu
- Swipe gestures for week navigation
- Larger touch targets (44x44px min)
- Bottom navigation bar option
"""
    },
    {
        "title": "[UX] Last Updated Timestamps",
        "milestone": "M5",
        "labels": ["type:ux", "priority:low"],
        "body": """## Overview
Show last modification date on each page.

## Features
- "Last updated: Dec 25, 2025" display
- "What's New" highlights for recent changes
- RSS feed for updates
- Git-based timestamps
"""
    },
    {
        "title": "[UX] Quick Reference Cards",
        "milestone": "M5",
        "labels": ["type:ux", "priority:low"],
        "body": """## Overview
Design printable one-page summaries per week.

## Content
- Key concepts (5-7 terms)
- Main algorithms
- Important formulas
- Paper references
- Code snippets

## Format
- PDF download
- Print-optimized CSS
- One page per week
"""
    },
    {
        "title": "[UX] Smart Prerequisites",
        "milestone": "M5",
        "labels": ["type:ux", "priority:low"],
        "body": """## Overview
Show prerequisite topics with links when starting a week.

## Implementation
- Define prerequisite graph in data file
- Show "Before starting, review:" section
- Link to relevant prior weeks
- Collapsible by default
"""
    },

    # ==================== MILESTONE 6: Technical Infrastructure (6 issues) ====================
    {
        "title": "[INFRA] Expand JSON API Endpoints",
        "milestone": "M6",
        "labels": ["type:infra", "priority:medium"],
        "body": """## Overview
Add more API endpoints for programmatic access.

## New Endpoints
- `/api/charts.json` - All chart metadata
- `/api/exercises.json` - Exercise listings
- `/api/papers.json` - Paper bibliography
- `/api/progress.json` - User progress (if authenticated)

## Implementation
- Jekyll data templates
- Consistent schema
- CORS headers
"""
    },
    {
        "title": "[INFRA] Privacy-Focused Analytics",
        "milestone": "M6",
        "labels": ["type:infra", "priority:medium"],
        "body": """## Overview
Configure Plausible or Umami analytics.

## Requirements
- No cookies
- No PII collection
- GDPR compliant
- Track: page views, popular content, referrers

## Implementation
- Add script tag to head_custom.html
- Configure dashboard
- Document in privacy policy
"""
    },
    {
        "title": "[INFRA] Lighthouse CI",
        "milestone": "M6",
        "labels": ["type:infra", "priority:medium"],
        "body": """## Overview
Require Lighthouse scores >90 before deploy.

## Metrics
- Performance: >90
- Accessibility: >90
- Best Practices: >90
- SEO: >90

## Implementation
- GitHub Action with lighthouse-ci
- Block PR merge if scores below threshold
- Report in PR comments
"""
    },
    {
        "title": "[INFRA] Content Sitemap",
        "milestone": "M6",
        "labels": ["type:infra", "priority:low"],
        "body": """## Overview
Generate XML sitemap and JSON content index.

## Files
- `sitemap.xml` - For search engines
- `content-index.json` - For internal search

## Implementation
- Jekyll plugins
- Auto-update on build
- Submit to Google Search Console
"""
    },
    {
        "title": "[INFRA] CDN Caching Strategy",
        "milestone": "M6",
        "labels": ["type:infra", "priority:low"],
        "body": """## Overview
Configure asset caching and cache busting.

## Strategy
- Static assets: 1 year cache
- HTML: No cache
- Versioned filenames for updates

## Implementation
- GitHub Pages headers
- Asset fingerprinting
- Service worker updates
"""
    },
    {
        "title": "[INFRA] Structured Data Markup",
        "milestone": "M6",
        "labels": ["type:infra", "priority:low"],
        "body": """## Overview
Implement schema.org markup for SEO.

## Schema Types
- Course
- LearningResource
- Article
- Person (instructor)
- Organization (institution)

## Implementation
- JSON-LD in head
- Validate with Google Rich Results Test
"""
    },

    # ==================== MILESTONE 7: Community Features (4 issues) ====================
    {
        "title": "[COMMUNITY] Enable GitHub Discussions",
        "milestone": "M7",
        "labels": ["type:community", "priority:low"],
        "body": """## Overview
Configure GitHub Discussions for course Q&A.

## Categories
- Q&A (questions with answers)
- Ideas (feature suggestions)
- Show and Tell (student projects)
- General (course discussions)

## Integration
- Link from each week page
- "Ask a Question" button
- Embed recent discussions widget
"""
    },
    {
        "title": "[COMMUNITY] Student Project Showcase",
        "milestone": "M7",
        "labels": ["type:community", "priority:low"],
        "body": """## Overview
Build gallery page for student projects.

## Features
- Project cards with screenshots
- Filter by semester/topic
- Submission form
- Featured projects section

## Page
- `docs/showcase.md`
"""
    },
    {
        "title": "[COMMUNITY] Hypothesis Annotations",
        "milestone": "M7",
        "labels": ["type:community", "priority:low"],
        "body": """## Overview
Enable collaborative annotations on content.

## Implementation
- Enable Hypothesis (already in includes, commented)
- Create course-specific group
- Document onboarding
- Moderate annotations
"""
    },
    {
        "title": "[COMMUNITY] Contribution Guidelines",
        "milestone": "M7",
        "labels": ["type:community", "priority:low"],
        "body": """## Overview
Write CONTRIBUTING.md with content standards.

## Sections
- How to contribute
- Content style guide
- PR process
- Local development setup
- Code of conduct
"""
    },

    # ==================== MILESTONE 8: Accessibility (4 issues) ====================
    {
        "title": "[A11Y] Full Accessibility Audit",
        "milestone": "M8",
        "labels": ["type:a11y", "priority:medium"],
        "body": """## Overview
Conduct comprehensive accessibility audit.

## Tools
- axe-core browser extension
- WAVE evaluation tool
- Manual screen reader testing (NVDA/VoiceOver)

## Standards
- WCAG 2.1 AA compliance
- Document all findings
- Create remediation plan
"""
    },
    {
        "title": "[A11Y] Alt Text for All Charts",
        "milestone": "M8",
        "labels": ["type:a11y", "priority:medium"],
        "body": """## Overview
Write descriptive alt text for all 48 charts.

## Requirements
- Describe data insights, not just titles
- Include key numbers/trends
- Keep under 125 characters
- Add long descriptions where needed

## Process
- Review each chart
- Write alt text
- Update week pages
- Document in data file
"""
    },
    {
        "title": "[A11Y] Skip Links and Focus Management",
        "milestone": "M8",
        "labels": ["type:a11y", "priority:medium"],
        "body": """## Overview
Improve keyboard navigation accessibility.

## Items
- Skip-to-content link (verify working)
- Focus indicators (high contrast)
- Logical tab order
- Focus trapping in modals
- Skip navigation option
"""
    },
    {
        "title": "[A11Y] Print Stylesheets",
        "milestone": "M8",
        "labels": ["type:a11y", "priority:low"],
        "body": """## Overview
Design printer-friendly layouts.

## Pages to Optimize
- Syllabus
- Week pages
- Quick reference cards
- Glossary

## Implementation
- Print media queries
- Hide navigation
- Optimize for A4/Letter
- Include URLs for links
"""
    },
]


def create_issue(issue_data):
    """Create a single GitHub issue using gh CLI."""
    title = issue_data["title"]
    body = issue_data["body"]
    milestone_title = MILESTONES[issue_data["milestone"]]
    labels = ",".join(issue_data["labels"])

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO,
        "--title", title,
        "--body", body,
        "--milestone", milestone_title,
        "--label", labels
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            # Extract issue number from URL
            url = result.stdout.strip()
            print(f"Created: {title} -> {url}")
            return True
        else:
            print(f"Failed: {title}")
            print(f"Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"Timeout: {title}")
        return False
    except Exception as e:
        print(f"Exception: {title} - {e}")
        return False


def main():
    """Create all 58 issues."""
    print(f"Creating {len(ISSUES)} issues...")
    print("=" * 60)

    success = 0
    failed = 0

    for i, issue in enumerate(ISSUES, 1):
        print(f"\n[{i}/{len(ISSUES)}] ", end="")
        if create_issue(issue):
            success += 1
        else:
            failed += 1
        # Small delay to avoid rate limiting
        time.sleep(0.5)

    print("\n" + "=" * 60)
    print(f"Done! Created: {success}, Failed: {failed}")


if __name__ == "__main__":
    main()
