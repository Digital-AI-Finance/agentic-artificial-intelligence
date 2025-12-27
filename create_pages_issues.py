"""Create GitHub Pages enhancement issues."""
import subprocess
import time

issues = [
    # Category 1: Site Structure and Navigation
    {
        "title": "[PAGES] Create Course Landing Page with Hero Section",
        "body": """## Description
Create a professional landing page for the course with:
- Hero section with course title, subtitle, and key value propositions
- Animated background or subtle visual effects
- Quick stats (12 weeks, X notebooks, X papers)
- Call-to-action buttons (Start Learning, View Syllabus, GitHub Repo)
- Instructor information with photo and credentials
- Institution branding (FHGR/Digital Finance)

## Acceptance Criteria
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Page loads in < 2 seconds
- [ ] Accessibility compliant (WCAG 2.1 AA)
- [ ] SEO meta tags included""",
        "labels": ["type:pages", "priority:critical", "enhancement"]
    },
    {
        "title": "[PAGES] Implement Sticky Navigation with Week Progress",
        "body": """## Description
Create a sticky navigation bar that:
- Shows current section/week
- Displays progress indicator (X/12 weeks)
- Provides quick links to all major sections
- Collapses elegantly on mobile
- Highlights current page in navigation

## Acceptance Criteria
- [ ] Navigation visible on scroll
- [ ] Smooth scroll to sections
- [ ] Mobile hamburger menu
- [ ] Active state highlighting""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Create Interactive Course Syllabus Page",
        "body": """## Description
Build a comprehensive syllabus page with:
- Week-by-week breakdown with expandable sections
- Learning objectives for each week
- Required vs. optional readings
- Assignment due dates
- Downloadable PDF version
- Calendar integration (ICS export)

## Acceptance Criteria
- [ ] All 12 weeks documented
- [ ] Expand/collapse functionality
- [ ] PDF export button
- [ ] ICS calendar download""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Build Week Detail Pages with Unified Template",
        "body": """## Description
Create individual pages for each week with consistent template:
- Week title and overview
- Learning objectives (Bloom's taxonomy)
- Lecture slides embed/download
- Notebook links with Colab badges
- Required readings with DOIs
- Exercises with rubrics
- Navigation to prev/next week

## Acceptance Criteria
- [ ] 12 week pages created
- [ ] Consistent styling
- [ ] All resources linked
- [ ] Mobile responsive""",
        "labels": ["type:pages", "priority:critical", "enhancement"]
    },
    # Category 2: Interactive Features
    {
        "title": "[PAGES] Add Interactive Code Playground with Pyodide",
        "body": """## Description
Embed interactive Python code cells that run in the browser:
- Use Pyodide for browser-based Python
- Pre-load common libraries (numpy, etc.)
- Allow code editing and execution
- Display output inline
- Save/share code snippets

## Acceptance Criteria
- [ ] Python code runs in browser
- [ ] Syntax highlighting
- [ ] Output display
- [ ] Error handling""",
        "labels": ["type:pages", "priority:medium", "feature"]
    },
    {
        "title": "[PAGES] Create Interactive Agent Architecture Diagrams",
        "body": """## Description
Build interactive diagrams using D3.js or Mermaid:
- ReAct loop visualization
- Multi-agent communication flows
- Tool use sequences
- Memory architectures
- Hover for details
- Click for deep dives

## Acceptance Criteria
- [ ] 5+ interactive diagrams
- [ ] Responsive sizing
- [ ] Tooltips on hover
- [ ] Smooth animations""",
        "labels": ["type:pages", "priority:medium", "feature"]
    },
    {
        "title": "[PAGES] Implement Concept Quiz System",
        "body": """## Description
Add self-assessment quizzes for each week:
- Multiple choice questions
- True/false questions
- Code completion challenges
- Immediate feedback
- Score tracking (local storage)
- Explanations for wrong answers

## Acceptance Criteria
- [ ] 5+ questions per week
- [ ] Instant feedback
- [ ] Progress saved locally
- [ ] Review mode available""",
        "labels": ["type:pages", "priority:medium", "feature"]
    },
    {
        "title": "[PAGES] Add Live Demo Agents",
        "body": """## Description
Embed live agent demonstrations:
- Simple ReAct agent demo
- Tool use demonstration
- Multi-agent chat simulation
- Uses free-tier API or simulated responses
- Shows thought/action/observation flow

## Acceptance Criteria
- [ ] At least 2 live demos
- [ ] Graceful fallback if API unavailable
- [ ] Clear visualization of agent reasoning""",
        "labels": ["type:pages", "priority:low", "feature"]
    },
    # Category 3: Content Presentation
    {
        "title": "[PAGES] Create Paper Reading List with Annotations",
        "body": """## Description
Build a comprehensive paper library page:
- All papers organized by week and topic
- Filterable by topic, year, author
- Searchable titles and abstracts
- Annotation highlights for key papers
- BibTeX export for each paper
- Citation counts from Semantic Scholar

## Acceptance Criteria
- [ ] 40+ papers catalogued
- [ ] Filter and search working
- [ ] DOI links verified
- [ ] BibTeX export functional""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Implement Glossary with Cross-References",
        "body": """## Description
Create a searchable glossary of terms:
- Alphabetical listing
- Search/filter functionality
- Links to relevant weeks
- Related terms cross-references
- Pronunciation guides where needed

## Acceptance Criteria
- [ ] 100+ terms defined
- [ ] Search functional
- [ ] Cross-references working
- [ ] Linked from week pages""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Add Code Snippet Gallery",
        "body": """## Description
Create a gallery of reusable code patterns:
- Categorized by topic (prompting, tools, agents)
- Syntax highlighted
- Copy to clipboard button
- Runnable in Colab link
- Tags for searchability

## Acceptance Criteria
- [ ] 30+ code snippets
- [ ] Copy functionality
- [ ] Category filtering
- [ ] Colab integration""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Create Comparison Tables for Frameworks/Models",
        "body": """## Description
Build interactive comparison tables:
- Agent frameworks (LangChain, LangGraph, AutoGen, CrewAI)
- LLM providers (OpenAI, Anthropic, Google, Open-source)
- Benchmarks (AgentBench, SWE-bench, GAIA)
- Sortable columns
- Expandable details

## Acceptance Criteria
- [ ] 4+ comparison tables
- [ ] Sortable columns
- [ ] Mobile scrollable
- [ ] Last updated dates""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    # Category 4: User Experience
    {
        "title": "[PAGES] Implement Dark Mode Toggle",
        "body": """## Description
Add dark mode support:
- Toggle button in navigation
- Respects system preference
- Persists choice in localStorage
- Smooth transition animation
- All elements properly themed

## Acceptance Criteria
- [ ] Toggle functional
- [ ] System preference detection
- [ ] Persistence working
- [ ] All pages themed""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Add Search Functionality with Lunr.js",
        "body": """## Description
Implement site-wide search:
- Search all content (weeks, papers, glossary)
- Real-time results as you type
- Keyboard shortcuts (Cmd/Ctrl + K)
- Result highlighting
- Recent searches history

## Acceptance Criteria
- [ ] Search indexes all content
- [ ] Results appear in < 200ms
- [ ] Keyboard navigation
- [ ] Mobile friendly""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Create Print-Friendly Stylesheets",
        "body": """## Description
Add print CSS for documentation:
- Clean, printer-friendly layouts
- Page breaks at logical points
- Hide navigation elements
- Include URLs for links
- QR codes for digital resources

## Acceptance Criteria
- [ ] Print preview looks clean
- [ ] No broken layouts
- [ ] Links printed as text""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    {
        "title": "[PAGES] Implement Reading Progress Indicator",
        "body": """## Description
Add progress bar showing scroll position:
- Thin bar at top of page
- Shows percentage read
- Smooth animation
- Optional estimated reading time

## Acceptance Criteria
- [ ] Progress bar visible
- [ ] Accurate percentage
- [ ] Performance optimized""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    # Category 5: Community and Collaboration
    {
        "title": "[PAGES] Add Discussion Links per Week",
        "body": """## Description
Integrate discussion functionality:
- Link to GitHub Discussions for each week
- Show recent discussion topics
- Direct link to ask questions
- FAQ section per week

## Acceptance Criteria
- [ ] Discussion links on all week pages
- [ ] GitHub Discussions enabled
- [ ] FAQ section populated""",
        "labels": ["type:pages", "priority:medium", "feature"]
    },
    {
        "title": "[PAGES] Create Student Project Showcase",
        "body": """## Description
Build a gallery for student projects:
- Project cards with images
- Brief descriptions
- Links to repositories
- Technologies used tags
- Submission form for new projects

## Acceptance Criteria
- [ ] Gallery layout working
- [ ] Filterable by cohort/topic
- [ ] Responsive grid
- [ ] Submission process documented""",
        "labels": ["type:pages", "priority:medium", "feature"]
    },
    {
        "title": "[PAGES] Add Contributor Recognition Page",
        "body": """## Description
Create a page recognizing contributors:
- Course instructors
- Teaching assistants
- Content contributors
- Pull request contributors (auto-generated)
- Acknowledgments section

## Acceptance Criteria
- [ ] All contributors listed
- [ ] Auto-fetch from GitHub API
- [ ] Profile pictures included""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    # Category 6: Technical Infrastructure
    {
        "title": "[PAGES] Set Up Jekyll Theme with Custom Styling",
        "body": """## Description
Configure Jekyll site with custom theme:
- Choose appropriate base theme (Just the Docs, Minimal Mistakes)
- Custom color palette matching course branding
- Typography system (Inter, JetBrains Mono for code)
- Component library (buttons, cards, alerts)
- Sass/SCSS organization

## Acceptance Criteria
- [ ] Theme configured
- [ ] Custom styles applied
- [ ] Build succeeds
- [ ] No style conflicts""",
        "labels": ["type:pages", "priority:critical", "type:infrastructure"]
    },
    {
        "title": "[PAGES] Implement Automated Build and Deploy",
        "body": """## Description
Set up GitHub Actions for site:
- Build on push to main
- Link checking
- HTML validation
- Lighthouse performance checks
- Deploy to GitHub Pages

## Acceptance Criteria
- [ ] Action runs on push
- [ ] Broken links reported
- [ ] Performance > 90
- [ ] Deploy automated""",
        "labels": ["type:pages", "priority:high", "type:infrastructure"]
    },
    {
        "title": "[PAGES] Add Analytics and Usage Tracking",
        "body": """## Description
Implement privacy-respecting analytics:
- Plausible or Umami (privacy-focused)
- Page view tracking
- Popular content identification
- No cookies required
- Dashboard for instructors

## Acceptance Criteria
- [ ] Analytics integrated
- [ ] GDPR compliant
- [ ] Dashboard accessible
- [ ] No PII collected""",
        "labels": ["type:pages", "priority:medium", "type:infrastructure"]
    },
    {
        "title": "[PAGES] Create JSON API for Course Data",
        "body": """## Description
Generate JSON endpoints for course data:
- /api/weeks.json - Week summaries
- /api/papers.json - Paper database
- /api/glossary.json - Terms
- /api/resources.json - All resources
- Enable programmatic access

## Acceptance Criteria
- [ ] JSON files generated
- [ ] Valid JSON schema
- [ ] CORS enabled
- [ ] Documentation provided""",
        "labels": ["type:pages", "priority:low", "type:infrastructure"]
    },
    {
        "title": "[PAGES] Implement Service Worker for Offline Access",
        "body": """## Description
Add PWA capabilities:
- Service worker for caching
- Offline page available
- Cache key resources
- Update notification
- Add to home screen

## Acceptance Criteria
- [ ] Service worker registered
- [ ] Offline page works
- [ ] Cache strategy defined
- [ ] Manifest.json created""",
        "labels": ["type:pages", "priority:low", "feature"]
    },
    # Category 7: Accessibility and Internationalization
    {
        "title": "[PAGES] Conduct Accessibility Audit and Fixes",
        "body": """## Description
Ensure full accessibility compliance:
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader testing
- Color contrast checking
- Alt text for all images
- Focus indicators

## Acceptance Criteria
- [ ] Lighthouse accessibility > 95
- [ ] axe-core passes
- [ ] Manual screen reader test
- [ ] Skip links implemented""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Add Language Toggle (EN/DE)",
        "body": """## Description
Prepare for internationalization:
- Language switcher in nav
- English as default
- German translation structure
- Content fallback system
- RTL preparation

## Acceptance Criteria
- [ ] Language toggle works
- [ ] At least landing page in DE
- [ ] Fallback to EN working""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    # Category 8: Content Enrichment
    {
        "title": "[PAGES] Create Getting Started Tutorial",
        "body": """## Description
Build an onboarding tutorial:
- Environment setup guide
- API key configuration
- First notebook walkthrough
- Troubleshooting common issues
- Video embed (optional)

## Acceptance Criteria
- [ ] Complete setup guide
- [ ] Screenshots included
- [ ] Platform-specific instructions
- [ ] Tested on fresh environment""",
        "labels": ["type:pages", "priority:high", "enhancement"]
    },
    {
        "title": "[PAGES] Add Research Paper Summaries",
        "body": """## Description
Create summaries for key papers:
- 1-page summary per paper
- Key contributions
- Method overview
- Results highlights
- Discussion questions
- 10+ paper summaries

## Acceptance Criteria
- [ ] Consistent format
- [ ] Linked from reading lists
- [ ] Author-verified accuracy""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Create Video Lecture Embeds",
        "body": """## Description
If video lectures exist, embed them:
- YouTube/Vimeo embeds
- Responsive video player
- Chapter markers if available
- Transcript links
- Playback speed hints

## Acceptance Criteria
- [ ] Videos embedded properly
- [ ] Responsive sizing
- [ ] Accessibility (captions)""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Build FAQ Page with Categories",
        "body": """## Description
Create comprehensive FAQ:
- Course logistics
- Technical setup
- Assignment questions
- Career/research guidance
- Expandable answers
- Search within FAQ

## Acceptance Criteria
- [ ] 30+ questions answered
- [ ] Categorized properly
- [ ] Search functional
- [ ] Updated regularly""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    # Category 9: Visual Enhancements
    {
        "title": "[PAGES] Design Custom Icons for Course Topics",
        "body": """## Description
Create custom iconography:
- Icon for each week/topic
- Consistent style (line/filled)
- SVG format for scaling
- Color variants
- Animation on hover

## Acceptance Criteria
- [ ] 12 week icons
- [ ] Additional UI icons
- [ ] SVG sprite sheet
- [ ] Usage documentation""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    {
        "title": "[PAGES] Add Animated Transitions Between Pages",
        "body": """## Description
Implement smooth page transitions:
- Fade or slide transitions
- Loading indicator
- Preserve scroll position
- Hardware accelerated

## Acceptance Criteria
- [ ] Transitions smooth
- [ ] No layout shifts
- [ ] Performance maintained""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    {
        "title": "[PAGES] Create Infographics for Key Concepts",
        "body": """## Description
Design infographics for:
- Agent architecture overview
- ReAct paradigm explanation
- Multi-agent patterns
- RAG pipeline
- Evaluation metrics

## Acceptance Criteria
- [ ] 5+ infographics
- [ ] High resolution
- [ ] Downloadable
- [ ] Properly attributed""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    # Category 10: Integration and Extensions
    {
        "title": "[PAGES] Integrate with Jupyter Book",
        "body": """## Description
Consider Jupyter Book integration:
- Evaluate Jupyter Book vs Jekyll
- If chosen, migrate content
- Execute notebooks in build
- Generate from notebooks
- MyST markdown support

## Acceptance Criteria
- [ ] Evaluation documented
- [ ] Migration plan if proceeding
- [ ] Notebook execution working""",
        "labels": ["type:pages", "priority:medium", "enhancement"]
    },
    {
        "title": "[PAGES] Add OpenAlex Widget for Paper Metrics",
        "body": """## Description
Embed live paper metrics:
- Citation counts from OpenAlex
- Trending papers widget
- Author profiles
- Real-time updates
- Cache for performance

## Acceptance Criteria
- [ ] Widget functional
- [ ] Metrics displayed
- [ ] Fallback for failures""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    {
        "title": "[PAGES] Create Zotero Collection Link",
        "body": """## Description
Link to Zotero reading list:
- Public Zotero group
- Embedded bibliography
- One-click add to Zotero
- Export formats (BibTeX, RIS)

## Acceptance Criteria
- [ ] Zotero collection created
- [ ] All papers added
- [ ] Link from site working""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    {
        "title": "[PAGES] Add Hypothesis Annotation Layer",
        "body": """## Description
Enable collaborative annotations:
- Hypothesis.is integration
- Course-specific group
- Highlight and comment
- Discussion threads on content

## Acceptance Criteria
- [ ] Hypothesis script added
- [ ] Group configured
- [ ] Student onboarding guide""",
        "labels": ["type:pages", "priority:low", "enhancement"]
    },
    # Category 11: Documentation
    {
        "title": "[PAGES] Create Site Contribution Guide",
        "body": """## Description
Document how to contribute:
- Content submission process
- Writing style guide
- Technical setup for local dev
- Pull request template
- Review process

## Acceptance Criteria
- [ ] CONTRIBUTING.md complete
- [ ] Style guide written
- [ ] Local dev instructions
- [ ] PR template created""",
        "labels": ["type:pages", "priority:medium", "documentation"]
    },
    {
        "title": "[PAGES] Write Content Style Guide",
        "body": """## Description
Establish content standards:
- Writing tone and voice
- Formatting conventions
- Code block standards
- Image specifications
- Citation format

## Acceptance Criteria
- [ ] Guide documented
- [ ] Examples provided
- [ ] Linting rules created""",
        "labels": ["type:pages", "priority:medium", "documentation"]
    },
    {
        "title": "[PAGES] Create Maintenance Runbook",
        "body": """## Description
Document maintenance tasks:
- How to update content
- Build troubleshooting
- Dependency updates
- Analytics review process
- Backup procedures

## Acceptance Criteria
- [ ] Runbook complete
- [ ] Tested procedures
- [ ] Contact information""",
        "labels": ["type:pages", "priority:low", "documentation"]
    },
]

def create_issue(issue):
    """Create a single GitHub issue."""
    labels = ",".join(issue["labels"])
    cmd = [
        "gh", "issue", "create",
        "--title", issue["title"],
        "--body", issue["body"],
        "--label", labels
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Created: {issue['title']}")
        return True
    else:
        print(f"Failed: {issue['title']}")
        print(f"  Error: {result.stderr}")
        return False

def main():
    print(f"Creating {len(issues)} GitHub Pages issues...")
    print("=" * 60)

    success = 0
    failed = 0

    for i, issue in enumerate(issues, 1):
        print(f"\n[{i}/{len(issues)}] ", end="")
        if create_issue(issue):
            success += 1
        else:
            failed += 1
        time.sleep(0.5)  # Rate limiting

    print("\n" + "=" * 60)
    print(f"Complete: {success} created, {failed} failed")

if __name__ == "__main__":
    main()
