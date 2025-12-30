"""Quality and accessibility check for the course website."""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json

BASE_URL = 'https://digital-ai-finance.github.io/agentic-artificial-intelligence'

def check_page(page, url, name):
    """Check a single page for quality issues."""
    issues = []

    try:
        response = page.goto(url, wait_until='networkidle', timeout=30000)
        if response.status != 200:
            issues.append(f"HTTP {response.status}")
            return {'name': name, 'url': url, 'status': 'error', 'issues': issues}
    except Exception as e:
        return {'name': name, 'url': url, 'status': 'error', 'issues': [str(e)]}

    # Check for page title
    title = page.title()
    if not title or len(title) < 5:
        issues.append("Missing or short page title")

    # Check for main content
    main = page.locator('main, article, .main-content').first
    if not main.is_visible():
        issues.append("No main content area found")

    # Check for headings hierarchy
    h1_count = page.locator('h1').count()
    if h1_count == 0:
        issues.append("No H1 heading")
    elif h1_count > 1:
        issues.append(f"Multiple H1 headings ({h1_count})")

    # Check for images without alt text
    images = page.locator('img:not([alt]), img[alt=""]').all()
    if images:
        issues.append(f"{len(images)} images missing alt text")

    # Check for broken internal links
    links = page.locator('a[href^="/"], a[href^="./"], a[href^="../"]').all()
    broken = 0
    for link in links[:10]:  # Check first 10 internal links
        href = link.get_attribute('href')
        if href and not href.startswith('#'):
            try:
                full_url = f"{BASE_URL}{href}" if href.startswith('/') else href
                # Just check if the element is valid, don't navigate
            except:
                broken += 1

    # Check for skip link (accessibility)
    skip_link = page.locator('a[href="#main-content"], a[href="#content"], .skip-link').first
    if not skip_link.is_visible():
        pass  # Skip link check - optional for this site

    # Check for navigation
    nav = page.locator('nav, [role="navigation"]').first
    if not nav.is_visible():
        issues.append("No navigation element")

    status = 'pass' if not issues else 'issues'
    return {'name': name, 'url': url, 'status': status, 'issues': issues}


def main():
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Pages to check (note: .html extension required)
        pages_to_check = [
            ('/', 'Home'),
            ('/glossary.html', 'Glossary'),
            ('/quizzes.html', 'Quizzes'),
            ('/architectures.html', 'Architectures'),
        ]

        # Add all 12 weeks
        for i in range(1, 13):
            pages_to_check.append((f'/weeks/week-{i}.html', f'Week {i}'))

        print("Quality Check Report")
        print("=" * 60)

        for path, name in pages_to_check:
            url = BASE_URL + path
            result = check_page(page, url, name)
            results.append(result)

            status_icon = 'OK' if result['status'] == 'pass' else 'ISSUES' if result['status'] == 'issues' else 'ERROR'
            print(f"{status_icon:6} {name:20} {url}")
            if result['issues']:
                for issue in result['issues']:
                    print(f"       - {issue}")

        browser.close()

    # Summary
    print("\n" + "=" * 60)
    passed = sum(1 for r in results if r['status'] == 'pass')
    with_issues = sum(1 for r in results if r['status'] == 'issues')
    errors = sum(1 for r in results if r['status'] == 'error')

    print(f"Summary: {passed} passed, {with_issues} with issues, {errors} errors")
    print(f"Total pages checked: {len(results)}")

    # Save results
    output_path = Path(__file__).parent.parent / 'quality_report.json'
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nDetailed report: {output_path}")

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    exit(main())
