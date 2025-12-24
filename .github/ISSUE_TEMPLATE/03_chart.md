---
name: Chart Development
about: Create a visualization chart for slides
title: '[CHART] L{XX}/{folder_name}: {Chart Description}'
labels: type:chart, priority:medium
assignees: ''
---

## Chart Description
{What this chart visualizes}

## Chart Type
- [ ] Concept diagram
- [ ] Data visualization
- [ ] Process flow
- [ ] Comparison chart
- [ ] Architecture diagram

## Location
- Lesson: L{XX}
- Folder: {folder_name}/
- Files: chart.py, chart.pdf

## Design Requirements
- [ ] Uses standard color palette (MLPURPLE, MLBLUE, etc.)
- [ ] figsize=(10, 6) for beamer compatibility
- [ ] Font sizes scaled for 70% display
- [ ] No plt.subplots() - single figure only

## Data Source
- [ ] Synthetic/simulated data (describe)
- [ ] Real dataset (specify source)
- [ ] Conceptual (no data needed)

## Acceptance Criteria
- [ ] chart.py follows template pattern
- [ ] Generates chart.pdf without errors
- [ ] Readable at 0.55-0.65\textwidth in beamer
- [ ] Uses Path(__file__).parent for output
