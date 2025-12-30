"""
Extract key terms from course slides for glossary generation.
Outputs JSON inventory compatible with docs/_data/glossary.yml

Usage:
    python scripts/extract_glossary.py
    python scripts/extract_glossary.py --output docs/_data/glossary_inventory.json
"""

import json
import re
import yaml
from pathlib import Path
from typing import Optional

# Project root
ROOT = Path(__file__).parent.parent

# Term categories with known terms
TERM_DEFINITIONS = {
    # === ACRONYMS ===
    "LLM": {
        "definition": "Large Language Model - neural network trained on text to generate and understand language",
        "category": "acronym",
        "related": ["GPT-4", "Claude", "Gemini"],
    },
    "ReAct": {
        "definition": "Reasoning and Acting paradigm that interleaves thought, action, and observation steps",
        "category": "paradigm",
        "related": ["Chain-of-Thought", "Agent Loop"],
        "source_paper": "Yao et al. 2023",
    },
    "CoT": {
        "definition": "Chain-of-Thought prompting - technique that elicits step-by-step reasoning",
        "category": "technique",
        "related": ["Tree-of-Thoughts", "Self-Consistency"],
        "source_paper": "Wei et al. 2022",
    },
    "ToT": {
        "definition": "Tree-of-Thoughts - framework that explores multiple reasoning paths",
        "category": "technique",
        "related": ["Chain-of-Thought", "Search"],
        "source_paper": "Yao et al. 2023",
    },
    "API": {
        "definition": "Application Programming Interface - structured interface for software communication",
        "category": "acronym",
        "related": ["Function Calling", "Tool Use"],
    },
    "MCP": {
        "definition": "Model Context Protocol - Anthropic's open standard for LLM-tool integration",
        "category": "protocol",
        "related": ["Tool Use", "Function Calling"],
    },
    "RAG": {
        "definition": "Retrieval-Augmented Generation - combining retrieval with generation for grounded responses",
        "category": "technique",
        "related": ["Self-RAG", "CRAG", "GraphRAG"],
    },
    "CRAG": {
        "definition": "Corrective RAG - system that evaluates and corrects poor retrievals before generation",
        "category": "technique",
        "related": ["RAG", "Self-RAG"],
        "source_paper": "Yan et al. 2024",
    },
    "LATS": {
        "definition": "Language Agent Tree Search - combines reasoning with Monte Carlo Tree Search",
        "category": "technique",
        "related": ["Planning", "Tree-of-Thoughts"],
        "source_paper": "Zhou et al. 2024",
    },
    # === CORE CONCEPTS ===
    "agent": {
        "definition": "Autonomous system that perceives its environment, reasons about it, and takes actions to achieve goals",
        "category": "concept",
        "related": ["Autonomous Agent", "LLM Agent", "Multi-Agent System"],
    },
    "trajectory": {
        "definition": "Complete sequence of states, actions, and observations an agent takes during task execution",
        "category": "concept",
        "related": ["Agent", "Episode", "ReAct"],
    },
    "observation": {
        "definition": "Feedback from the environment after an agent takes an action",
        "category": "concept",
        "related": ["Action", "State", "ReAct"],
    },
    "tool use": {
        "definition": "Ability of an agent to invoke external tools or APIs to accomplish tasks",
        "category": "concept",
        "related": ["Function Calling", "MCP"],
    },
    "planning": {
        "definition": "Process of decomposing complex tasks into manageable steps before execution",
        "category": "concept",
        "related": ["Reasoning", "Task Decomposition"],
    },
    "memory": {
        "definition": "System for storing and retrieving information across agent interactions",
        "category": "concept",
        "related": ["Short-term Memory", "Long-term Memory", "Episodic Memory"],
    },
    "hallucination": {
        "definition": "When an LLM generates plausible but factually incorrect information",
        "category": "concept",
        "related": ["Verification", "Grounding", "FActScore"],
    },
    "alignment": {
        "definition": "Training AI systems to follow human values and intentions",
        "category": "concept",
        "related": ["Safety", "Constitutional AI"],
    },
    "context window": {
        "definition": "Maximum number of tokens an LLM can process in a single interaction",
        "category": "concept",
        "related": ["Token", "Memory"],
    },
    "token": {
        "definition": "Basic unit of text processing in LLMs, roughly equivalent to 3/4 of a word",
        "category": "concept",
        "related": ["Context Window", "Tokenization"],
    },
    # === ARCHITECTURES ===
    "reactive": {
        "definition": "Agent architecture using direct stimulus-response without planning (simple reflex)",
        "category": "architecture",
        "related": ["Deliberative", "Hybrid"],
    },
    "deliberative": {
        "definition": "Agent architecture that plans before executing (model-based)",
        "category": "architecture",
        "related": ["Reactive", "Planning"],
    },
    "hybrid": {
        "definition": "Agent architecture combining reactive and deliberative layers",
        "category": "architecture",
        "related": ["Reactive", "Deliberative"],
    },
    "single-agent": {
        "definition": "Architecture where one LLM handles all tasks",
        "category": "architecture",
        "related": ["Multi-Agent", "Hierarchical"],
    },
    "multi-agent": {
        "definition": "Architecture where specialized agents collaborate on tasks",
        "category": "architecture",
        "related": ["Single-Agent", "Hierarchical", "Orchestration"],
    },
    "hierarchical": {
        "definition": "Architecture where manager agents delegate to worker agents",
        "category": "architecture",
        "related": ["Multi-Agent", "Orchestration"],
    },
    # === MEMORY TYPES ===
    "short-term memory": {
        "definition": "In-context memory stored within the current conversation",
        "category": "memory_type",
        "related": ["Long-term Memory", "Context Window"],
    },
    "long-term memory": {
        "definition": "Persistent storage across sessions (vector DB, knowledge graph)",
        "category": "memory_type",
        "related": ["Short-term Memory", "Vector Store"],
    },
    "vector store": {
        "definition": "Embedding database for semantic similarity search",
        "category": "memory_type",
        "related": ["RAG", "Embedding", "ChromaDB"],
    },
    "knowledge graph": {
        "definition": "Structured entity-relationship database for representing knowledge",
        "category": "memory_type",
        "related": ["GraphRAG", "Entity Extraction"],
    },
    "episodic memory": {
        "definition": "Memory system storing past experiences and reflections for future reference",
        "category": "memory_type",
        "related": ["Reflexion", "Long-term Memory"],
    },
    # === FRAMEWORKS ===
    "LangChain": {
        "definition": "Python framework for building LLM applications using chains of components",
        "category": "framework",
        "related": ["LangGraph", "LCEL"],
    },
    "LangGraph": {
        "definition": "LangChain's framework for building stateful, multi-actor applications using graphs",
        "category": "framework",
        "related": ["LangChain", "State Machine"],
    },
    "AutoGen": {
        "definition": "Microsoft's framework for building multi-agent conversational systems",
        "category": "framework",
        "related": ["Multi-Agent", "Conversation"],
    },
    "CrewAI": {
        "definition": "Framework for building role-playing autonomous AI agents that collaborate",
        "category": "framework",
        "related": ["Multi-Agent", "Roles"],
    },
    "Semantic Kernel": {
        "definition": "Microsoft's SDK for integrating LLMs with conventional programming",
        "category": "framework",
        "related": ["LangChain", "SDK"],
    },
    # === SYSTEMS ===
    "GPT-4": {
        "definition": "OpenAI's large language model powering ChatGPT and API",
        "category": "system",
        "related": ["LLM", "OpenAI"],
    },
    "Claude": {
        "definition": "Anthropic's large language model with Constitutional AI safety",
        "category": "system",
        "related": ["LLM", "Constitutional AI"],
    },
    "Gemini": {
        "definition": "Google's multimodal large language model",
        "category": "system",
        "related": ["LLM", "Google"],
    },
    "GitHub Copilot": {
        "definition": "AI-powered code completion and generation tool",
        "category": "system",
        "related": ["Code Agent", "IDE"],
    },
    "Devin": {
        "definition": "Cognition's autonomous software engineering agent",
        "category": "system",
        "related": ["Code Agent", "SWE-bench"],
    },
    "AutoGPT": {
        "definition": "Goal-directed autonomous agent that chains LLM calls",
        "category": "system",
        "related": ["Agent", "Autonomous"],
    },
    "BabyAGI": {
        "definition": "Task-driven autonomous agent using task prioritization",
        "category": "system",
        "related": ["Agent", "Task Management"],
    },
    "Voyager": {
        "definition": "NVIDIA's open-ended embodied agent for Minecraft exploration",
        "category": "system",
        "related": ["Embodied Agent", "Curriculum Learning"],
        "source_paper": "Wang et al. 2023",
    },
    # === TECHNIQUES ===
    "Chain-of-Thought": {
        "definition": "Prompting technique that elicits step-by-step reasoning from language models",
        "category": "technique",
        "related": ["CoT", "Reasoning"],
        "source_paper": "Wei et al. 2022",
    },
    "Tree-of-Thoughts": {
        "definition": "Framework that explores multiple reasoning paths and evaluates them",
        "category": "technique",
        "related": ["ToT", "Search"],
        "source_paper": "Yao et al. 2023",
    },
    "Self-Consistency": {
        "definition": "Sampling multiple reasoning paths and selecting the most common answer",
        "category": "technique",
        "related": ["Chain-of-Thought", "Ensemble"],
    },
    "Reflexion": {
        "definition": "Framework where agents learn from verbal self-reflection on past failures",
        "category": "technique",
        "related": ["Self-Improvement", "Memory"],
        "source_paper": "Shinn et al. 2023",
    },
    "Self-RAG": {
        "definition": "RAG system that learns when to retrieve and how to critique its own outputs",
        "category": "technique",
        "related": ["RAG", "Self-Improvement"],
        "source_paper": "Asai et al. 2023",
    },
    "GraphRAG": {
        "definition": "RAG approach using knowledge graphs for structured, multi-hop retrieval",
        "category": "technique",
        "related": ["RAG", "Knowledge Graph"],
        "source_paper": "Edge et al. 2024",
    },
    "function calling": {
        "definition": "API feature allowing LLMs to generate structured calls to predefined functions",
        "category": "technique",
        "related": ["Tool Use", "JSON Schema"],
    },
    "task decomposition": {
        "definition": "Breaking complex tasks into smaller, manageable subtasks",
        "category": "technique",
        "related": ["Planning", "Hierarchical"],
    },
    "Chain-of-Verification": {
        "definition": "Technique to reduce hallucinations through independent verification of claims",
        "category": "technique",
        "related": ["Hallucination", "Verification"],
        "source_paper": "Dhuliawala et al. 2023",
    },
    # === METRICS ===
    "AgentBench": {
        "definition": "Benchmark for evaluating LLMs as agents across multiple environments",
        "category": "metric",
        "related": ["Evaluation", "Benchmark"],
        "source_paper": "Liu et al. 2023",
    },
    "SWE-bench": {
        "definition": "Benchmark for evaluating code agents on real GitHub issues",
        "category": "metric",
        "related": ["Code Agent", "Evaluation"],
        "source_paper": "Jimenez et al. 2024",
    },
    "FActScore": {
        "definition": "Metric for evaluating factual precision in long-form text generation",
        "category": "metric",
        "related": ["Hallucination", "Evaluation"],
        "source_paper": "Min et al. 2023",
    },
    "Pass@k": {
        "definition": "Metric measuring success rate when k attempts are allowed",
        "category": "metric",
        "related": ["Evaluation", "Code Generation"],
    },
    # === SAFETY ===
    "Constitutional AI": {
        "definition": "Approach to AI safety using principles to guide self-improvement",
        "category": "safety",
        "related": ["Alignment", "RLHF"],
        "source_paper": "Bai et al. 2022",
    },
    "jailbreak": {
        "definition": "Technique to bypass LLM safety restrictions through adversarial prompts",
        "category": "safety",
        "related": ["Safety", "Adversarial"],
    },
    # === ADDITIONAL TERMS ===
    "orchestration": {
        "definition": "Coordination pattern where a central agent manages workflow across multiple agents",
        "category": "concept",
        "related": ["Multi-Agent", "Workflow"],
    },
    "embodied agent": {
        "definition": "Agent that interacts with a physical or simulated environment through sensors and actuators",
        "category": "concept",
        "related": ["Robotics", "Simulation"],
    },
    "world model": {
        "definition": "Internal representation of environment dynamics used for planning",
        "category": "concept",
        "related": ["Planning", "Simulation"],
    },
    "RAPTOR": {
        "definition": "Recursive Abstractive Processing for Tree-Organized Retrieval",
        "category": "technique",
        "related": ["RAG", "Hierarchical"],
    },
    "entity extraction": {
        "definition": "Process of identifying and extracting named entities from text",
        "category": "technique",
        "related": ["NER", "Knowledge Graph"],
    },
    "claim decomposition": {
        "definition": "Breaking down text into atomic, independently verifiable claims",
        "category": "technique",
        "related": ["Verification", "Fact-Checking"],
    },
    "LLM-as-Judge": {
        "definition": "Using an LLM to evaluate the quality of outputs from another model or agent",
        "category": "technique",
        "related": ["Evaluation", "Automated Assessment"],
    },
    "Generative Agent": {
        "definition": "Agent that simulates human behavior in interactive environments",
        "category": "concept",
        "related": ["Simulation", "Emergence"],
        "source_paper": "Park et al. 2023",
    },
    "emergent behavior": {
        "definition": "Complex behaviors arising from simple agent interactions",
        "category": "concept",
        "related": ["Multi-Agent", "Complexity"],
    },
}

# Regex patterns for finding terms in LaTeX
TERM_PATTERNS = {
    term: re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
    for term in TERM_DEFINITIONS.keys()
}


def extract_week_number(path: Path) -> int:
    """Extract week number from lecture folder name."""
    match = re.match(r'L(\d+)_', path.parent.name)
    if match:
        return int(match.group(1))
    return 0


def extract_slide_number(content: str, line_num: int) -> int:
    """Estimate slide number from line number by counting frame environments."""
    lines = content[:content.find('\n' * line_num)].split('\n') if line_num > 0 else []
    slide_count = 0
    for line in lines[:line_num]:
        if r'\begin{frame}' in line:
            slide_count += 1
    return max(1, slide_count)


def find_first_occurrence(tex_path: Path) -> dict[str, dict]:
    """Find first occurrence of each term in a .tex file."""
    content = tex_path.read_text(encoding='utf-8')
    lines = content.split('\n')
    occurrences = {}

    for term, pattern in TERM_PATTERNS.items():
        for line_num, line in enumerate(lines, 1):
            if pattern.search(line):
                # Check if term is defined at this location
                is_defined = False
                # Look for common definition patterns
                definition_patterns = [
                    rf'{re.escape(term)}\s*[:-]',  # "Term: definition" or "Term - definition"
                    rf'{re.escape(term)}\s*\([^)]+\)',  # "Term (explanation)"
                    rf'\\textbf{{{re.escape(term)}}}',  # Bold term (often definitions)
                    rf'{re.escape(term)}.*is\s+(a|an|the)',  # "Term is a..."
                    rf'define\s+{re.escape(term)}',  # "define Term"
                ]
                for def_pattern in definition_patterns:
                    if re.search(def_pattern, line, re.IGNORECASE):
                        is_defined = True
                        break

                occurrences[term] = {
                    "line": line_num,
                    "slide": extract_slide_number(content, line_num),
                    "context": line.strip()[:100],
                    "defined_at_first_use": is_defined,
                }
                break  # Only first occurrence

    return occurrences


def process_all_lectures() -> list[dict]:
    """Process all lecture .tex files and build glossary inventory."""
    glossary = []

    # Find all lecture .tex files
    tex_files = sorted(ROOT.glob("L*_*/*.tex"))

    # Track first occurrence across all lectures
    first_occurrences: dict[str, dict] = {}

    for tex_path in tex_files:
        if tex_path.stem.startswith("L") and "_" in tex_path.stem:
            week = extract_week_number(tex_path)
            occurrences = find_first_occurrence(tex_path)

            for term, occurrence in occurrences.items():
                if term not in first_occurrences:
                    first_occurrences[term] = {
                        "term": term,
                        "week": week,
                        "file": str(tex_path.relative_to(ROOT)),
                        **occurrence,
                    }

    # Build final glossary with definitions
    for term, data in TERM_DEFINITIONS.items():
        entry = {
            "term": term,
            "definition": data["definition"],
            "category": data["category"],
            "related_terms": data.get("related", []),
        }

        if "source_paper" in data:
            entry["source_paper"] = data["source_paper"]

        # Add first occurrence info if found
        if term in first_occurrences:
            occ = first_occurrences[term]
            entry["first_use"] = {
                "week": occ["week"],
                "slide": occ["slide"],
                "line": occ["line"],
                "file": occ["file"],
            }
            entry["defined_at_first_use"] = occ["defined_at_first_use"]
        else:
            entry["first_use"] = None
            entry["defined_at_first_use"] = None

        glossary.append(entry)

    # Sort by week of first use, then alphabetically
    glossary.sort(key=lambda x: (
        x["first_use"]["week"] if x["first_use"] else 99,
        x["term"].lower()
    ))

    return glossary


def merge_with_existing_glossary(new_terms: list, existing_path: Path) -> list:
    """Merge new terms with existing glossary.yml."""
    if not existing_path.exists():
        return new_terms

    with open(existing_path, 'r', encoding='utf-8') as f:
        existing = yaml.safe_load(f)

    if not existing:
        return new_terms

    # Create lookup of existing terms
    existing_terms = {item['term']: item for item in existing if 'term' in item}

    # Merge: prefer new definitions but keep existing week assignments
    merged = []
    seen = set()

    for new_entry in new_terms:
        term = new_entry['term']
        seen.add(term.lower())

        if term in existing_terms:
            # Merge with existing
            existing_entry = existing_terms[term]
            merged_entry = {**new_entry}
            # Keep existing week if present
            if 'week' in existing_entry and existing_entry['week']:
                merged_entry['week'] = existing_entry['week']
            merged.append(merged_entry)
        else:
            merged.append(new_entry)

    # Add any existing terms not in new list
    for term, entry in existing_terms.items():
        if term.lower() not in seen:
            merged.append({
                "term": term,
                "definition": entry.get('definition', ''),
                "category": "concept",
                "related_terms": entry.get('related', []),
                "first_use": {"week": entry.get('week', 0)},
                "defined_at_first_use": None,
            })

    return merged


def generate_statistics(glossary: list) -> dict:
    """Generate statistics about the glossary."""
    stats = {
        "total_terms": len(glossary),
        "by_category": {},
        "by_week": {},
        "defined_at_first_use": 0,
        "not_defined_at_first_use": 0,
        "not_found_in_slides": 0,
    }

    for entry in glossary:
        # By category
        cat = entry.get("category", "unknown")
        stats["by_category"][cat] = stats["by_category"].get(cat, 0) + 1

        # By week
        if entry.get("first_use"):
            week = entry["first_use"].get("week", 0)
            stats["by_week"][week] = stats["by_week"].get(week, 0) + 1

            # Definition status
            if entry.get("defined_at_first_use"):
                stats["defined_at_first_use"] += 1
            else:
                stats["not_defined_at_first_use"] += 1
        else:
            stats["not_found_in_slides"] += 1

    return stats


def main():
    """Generate complete glossary inventory."""
    import argparse

    parser = argparse.ArgumentParser(description="Extract glossary from course slides")
    parser.add_argument(
        "--output",
        default="docs/_data/glossary_inventory.json",
        help="Output JSON file path",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge with existing glossary.yml",
    )
    args = parser.parse_args()

    print("Extracting terms from lecture slides...")
    glossary = process_all_lectures()

    if args.merge:
        existing_path = ROOT / "docs" / "_data" / "glossary.yml"
        print(f"Merging with existing glossary at {existing_path}...")
        glossary = merge_with_existing_glossary(glossary, existing_path)

    # Generate statistics
    stats = generate_statistics(glossary)

    output = {
        "metadata": {
            "generated_from": "scripts/extract_glossary.py",
            "total_terms": stats["total_terms"],
            "statistics": stats,
        },
        "glossary": glossary,
    }

    output_path = ROOT / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nGlossary inventory saved to: {output_path}")
    print(f"\nStatistics:")
    print(f"  Total terms: {stats['total_terms']}")
    print(f"  By category: {stats['by_category']}")
    print(f"  Defined at first use: {stats['defined_at_first_use']}")
    print(f"  NOT defined at first use: {stats['not_defined_at_first_use']}")
    print(f"  Not found in slides: {stats['not_found_in_slides']}")


if __name__ == "__main__":
    main()
