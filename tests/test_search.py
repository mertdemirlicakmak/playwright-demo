from datetime import datetime, timedelta
from pytest_bdd import scenarios, given, when, then

# Link the feature file with the step definitions
scenarios("../features/basic_search.feature")


@given("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def navigate_to_homepage(homepage):
    pass  # The homepage is already opened in the fixture


@when("I select one-way trip type")
def select_one_way_trip(homepage):
    homepage.select_one_way_trip()


@when("Set as departure airport RTM")
def set_departure_airport(homepage):
    homepage.set_departure_airport("RTM")


@when("Set the arrival Airport MAD")
def set_arrival_airport(homepage):
    homepage.set_arrival_airport("MAD")


@when("Set the departure time 1 week in the future starting current date")
def set_departure_date(homepage):
    date_in_one_week = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    homepage.set_departure_date(date_in_one_week)


@when("Uncheck the `Check accommodation with booking.com` option")
def uncheck_booking_checkbox(homepage):
    homepage.uncheck_booking_checkbox()


@when("Click the search button")
def click_search_button(homepage):
    homepage.click_search_button()


@then("I am redirected to search results page")
def verify_search_results(homepage):
    current_url = homepage.page.url
    # assert "search/results" in current_url
    assert "search=results" in current_url
