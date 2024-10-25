import pytest
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright
from kiwi_home_page import KiwiHomePage
from pytest_bdd import scenarios, given, when, then

# Link the feature file with the step definitions
scenarios("features/basic_search.feature")


@pytest.fixture
def page_context():
    with sync_playwright() as p:
        # Set headless=False to see the browser window
        browser = p.chromium.launch(
            headless=False, slow_mo=600
        )  # slow_mo slows down actions for better visualization
        page = browser.new_page()
        yield page
        browser.close()


@given("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def navigate_to_homepage(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.open()
    homepage.click_close_cookies_window()


@when("I select one-way trip type")
def select_one_way_trip(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.select_one_way_trip()


@when("Set as departure airport RTM")
def set_departure_airport(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.set_departure_airport("RTM")


@when("Set the arrival Airport MAD")
def set_arrival_airport(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.set_arrival_airport("MAD")


@when("Set the departure time 1 week in the future starting current date")
def set_departure_date(page_context):
    date_in_one_week = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    homepage = KiwiHomePage(page_context)
    homepage.set_departure_date(date_in_one_week)


@when("Uncheck the `Check accommodation with booking.com` option")
def uncheck_booking_checkbox(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.uncheck_booking_checkbox()


@when("Click the search button")
def click_search_button(page_context):
    homepage = KiwiHomePage(page_context)
    homepage.click_search_button()


@then("I am redirected to search results page")
def verify_search_results(page_context):
    assert "search/results" in page_context.url
