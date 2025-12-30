"""Take a screenshot of the course website to verify all 12 weeks are visible."""
from playwright.sync_api import sync_playwright
from pathlib import Path

def main():
    output_path = Path(__file__).parent.parent / "website_screenshot.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        print("Navigating to course website...")
        page.goto('https://digital-ai-finance.github.io/agentic-artificial-intelligence/')
        page.wait_for_load_state('networkidle')

        # Wait a bit more for any JavaScript to finish
        page.wait_for_timeout(2000)

        # Check for 12 weeks
        week_links = page.locator('a:has-text("Week")').all()
        print(f"Found {len(week_links)} week links")

        # Take full-page screenshot
        page.screenshot(path=str(output_path), full_page=True)
        print(f"Screenshot saved to: {output_path}")

        # Print page title
        title = page.title()
        print(f"Page title: {title}")

        browser.close()

if __name__ == "__main__":
    main()
