from datetime import datetime
import os
import pytest
from playwright.sync_api import sync_playwright
from poms.kiwi_home_page import KiwiHomePage


@pytest.fixture
def page_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=300,
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.179 Safari/537.36"
        )
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def homepage(page_context):
    home = KiwiHomePage(page_context)
    home.open()
    home.click_close_cookies_window()
    return home


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request, page_context):
    yield
    # If the test fails, capture a screenshot
    if request.node.rep_call.failed:
        # Create the screenshots directory if it doesn't exist
        os.makedirs("test-reports/screenshots", exist_ok=True)

        # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"test-reports/screenshots/screenshot_{timestamp}.png"

        # Capture the screenshot
        page_context.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
