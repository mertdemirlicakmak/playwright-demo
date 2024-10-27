from playwright.sync_api import Page


class KiwiHomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.close_cookies_window_button = "//button[@aria-label='Close']"
        self.return_type_picker_button = (
            "//div[@data-test='SearchFormModesPicker-active-return']"
        )
        self.one_way_button = "//a[@data-test='ModePopupOption-oneWay___']"
        self.departure_input = "//div[@data-test='SearchFieldItem-origin']//input"
        self.arrival_input = "//div[@data-test='SearchFieldItem-destination']//input"
        self.departure_date_input = "//div[@data-test='SearchDateInput']"
        self.search_button = "//a[@data-test='LandingSearchButton']"
        self.departure_calendar_button = "//div[contains(@data-test, 'SearchDateInput')]//div[contains(text(), 'Departure')]"
        self.set_dates_done_button = "//button[@data-test='SearchFormDoneButton']"
        self.booking_checkbox = "//div[@data-test='bookingCheckbox']"

    def open(self):
        self.page.goto("https://www.kiwi.com/en/")

    def click_close_cookies_window(self):
        self.page.click(self.close_cookies_window_button)

    def select_one_way_trip(self):
        self.page.click(self.return_type_picker_button)
        self.page.click(self.one_way_button)

    def set_departure_airport(self, airport_code: str):
        self.page.click(self.departure_input)
        self.page.keyboard.press("Backspace")
        self.page.keyboard.press("Backspace")
        self.page.fill(self.departure_input, airport_code)
        self.page.click(
            f"//div[@data-test='PlacePickerRow-station']//div[contains(text(), '{airport_code}')]"
        )

    def set_arrival_airport(self, airport_code: str):
        self.page.click(self.arrival_input)
        self.page.keyboard.press("Backspace")
        self.page.keyboard.press("Backspace")
        self.page.fill(self.arrival_input, airport_code)
        self.page.click(
            f"//div[@data-test='PlacePickerRow-station']//div[contains(text(), '{airport_code}')]"
        )

    def set_departure_date(self, date: str):
        self.page.click(self.departure_calendar_button)
        self.page.click(
            f"//div[@data-test='CalendarDay' and contains(@data-value, '{date}')]"
        )
        self.page.click(self.set_dates_done_button)

    def uncheck_booking_checkbox(self):
        self.page.click(self.booking_checkbox)
        # if self.page.is_checked(self.booking_checkbox):
        #    self.page.click(self.booking_checkbox)

    def click_search_button(self):
        self.page.click(self.search_button)
