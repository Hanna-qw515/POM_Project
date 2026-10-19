from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RadioButtonPage(BasePage):
    URL = "https://demoqa.com/radio-button"
    # локаторы
    YES_INPUT = (By.ID, 'yesRadio')
    NO_INPUT = (By.ID, "noRadio")
    YES_LABEL_INPUT = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_LABEL_INPUT = (By.XPATH, "//label[@for='impressiveRadio']")
    TEXT_SUCCESS = (By.XPATH, "//span[@class='text-success']")

    def open_page(self):
        self.open(self.URL)

    def choose_yes(self):
        return self.click(self.YES_LABEL_INPUT)

    def choose_impressive(self):
        return self.click(self.IMPRESSIVE_LABEL_INPUT)

    def get_result(self):
        return self.get_text(self.TEXT_SUCCESS)

    def is_yes_selected(self):
        click_input = self.find(self.YES_INPUT)
        return click_input.is_selected()

    def is_no_enabled(self):
        disabled_no = self.find(self.NO_INPUT)
        return disabled_no.is_enabled()
