"""
Generate cross-lecture term index showing term progression across weeks.
Creates both JSON data and markdown visualization.
"""

import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent

# Import term definitions from extract_glossary
from extract_glossary import TERM_DEFINITIONS, TERM_VARIANTS


def find_all_occurrences() -> dict:
    """Find all occurrences of each term across all lectures."""
    term_occurrences = defaultdict(lambda: defaultdict(list))

    # Build patterns
    patterns = {}
    for term in TERM_DEFINITIONS.keys():
        variants = TERM_VARIANTS.get(term, [term])
        pattern_parts = [re.escape(v) for v in variants]
        combined_pattern = r'\b(' + '|'.join(pattern_parts) + r')\b'
        patterns[term] = re.compile(combined_pattern, re.IGNORECASE)

    # Process all lecture files
    tex_files = sorted(ROOT.glob("L*_*/*.tex"))

    for tex_path in tex_files:
        if not tex_path.stem.startswith("L"):
            continue

        # Extract week number
        match = re.match(r'L(\d+)_', tex_path.parent.name)
        if not match:
            continue
        week = int(match.group(1))

        content = tex_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        # Find current slide
        current_slide = 0
        for line_num, line in enumerate(lines, 1):
            if r'\begin{frame}' in line:
                current_slide += 1

            for term, pattern in patterns.items():
                if pattern.search(line):
                    term_occurrences[term][week].append({
                        "slide": current_slide,
                        "line": line_num
                    })

    return term_occurrences


def generate_term_matrix(occurrences: dict) -> dict:
    """Generate a term x week matrix showing where each term appears."""
    matrix = {}

    for term in sorted(TERM_DEFINITIONS.keys(), key=str.lower):
        weeks_present = sorted(occurrences[term].keys())
        matrix[term] = {
            "category": TERM_DEFINITIONS[term]["category"],
            "weeks": weeks_present,
            "first_week": min(weeks_present) if weeks_present else None,
            "occurrences": len(weeks_present),
            "details": {
                week: len(slides) for week, slides in occurrences[term].items()
            }
        }

    return matrix


def generate_markdown_index(matrix: dict) -> str:
    """Generate markdown table showing term progression."""
    lines = [
        "# Cross-Lecture Term Index",
        "",
        "This index shows which glossary terms appear in each week's lecture.",
        "",
        "## Term Matrix",
        "",
        "| Term | Cat. | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 |",
        "|------|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|",
    ]

    for term, data in sorted(matrix.items(), key=lambda x: x[0].lower()):
        cat = data["category"][:4]
        week_cells = []
        for w in range(1, 13):
            if w in data["weeks"]:
                count = data["details"].get(w, 0)
                week_cells.append(f"{count}" if count > 0 else "-")
            else:
                week_cells.append("-")
        row = f"| {term[:25]} | {cat} | " + " | ".join(week_cells) + " |"
        lines.append(row)

    lines.extend([
        "",
        "## Statistics",
        "",
        f"- Total terms: {len(matrix)}",
        f"- Terms appearing in 1 week: {sum(1 for d in matrix.values() if d['occurrences'] == 1)}",
        f"- Terms appearing in 2+ weeks: {sum(1 for d in matrix.values() if d['occurrences'] >= 2)}",
        f"- Terms appearing in 5+ weeks: {sum(1 for d in matrix.values() if d['occurrences'] >= 5)}",
        "",
        "## Category Legend",
        "",
        "- **acr**: Acronym",
        "- **arc**: Architecture",
        "- **con**: Concept",
        "- **fra**: Framework",
        "- **mem**: Memory Type",
        "- **met**: Metric",
        "- **par**: Paradigm",
        "- **pro**: Protocol",
        "- **saf**: Safety",
        "- **sys**: System",
        "- **tec**: Technique",
    ])

    return "\n".join(lines)


def generate_week_focus(matrix: dict) -> dict:
    """Generate per-week term focus summary."""
    week_focus = {w: {"new": [], "continued": []} for w in range(1, 13)}

    for term, data in matrix.items():
        if data["first_week"]:
            first = data["first_week"]
            week_focus[first]["new"].append(term)

            for week in data["weeks"]:
                if week != first:
                    week_focus[week]["continued"].append(term)

    return week_focus


def main():
    print("Generating cross-lecture term index...")

    occurrences = find_all_occurrences()
    matrix = generate_term_matrix(occurrences)
    week_focus = generate_week_focus(matrix)

    # Save JSON data
    output_json = ROOT / "docs" / "_data" / "term_index.json"
    output_json.parent.mkdir(parents=True, exist_ok=True)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({
            "matrix": matrix,
            "week_focus": week_focus,
            "statistics": {
                "total_terms": len(matrix),
                "by_category": defaultdict(int),
            }
        }, f, indent=2, ensure_ascii=False)

    print(f"Saved JSON: {output_json}")

    # Generate markdown
    markdown = generate_markdown_index(matrix)
    output_md = ROOT / "docs" / "term-index.md"

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write("layout: default\n")
        f.write("title: Term Index\n")
        f.write("nav_order: 15\n")
        f.write("---\n\n")
        f.write(markdown)

    print(f"Saved markdown: {output_md}")

    # Print summary
    print(f"\nSummary:")
    print(f"  Total terms indexed: {len(matrix)}")

    # Find most cross-cutting terms
    cross_cutting = [(t, d["occurrences"]) for t, d in matrix.items() if d["occurrences"] >= 4]
    cross_cutting.sort(key=lambda x: -x[1])

    if cross_cutting:
        print(f"\n  Most cross-cutting terms (4+ weeks):")
        for term, count in cross_cutting[:10]:
            print(f"    - {term}: {count} weeks")


if __name__ == "__main__":
    main()
