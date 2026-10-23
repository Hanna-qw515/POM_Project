from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class TextBoxPage(BasePage):
    URL = "https://demoqa.com/elements"
    TEXT_BUTTON = (By.ID, "item-0")
    #PART = "text-box"
    def open_page(self):
        self.open(self.URL)

    def text_button(self):
        return self.click(self.TEXT_BUTTON)

    def wait_url_contains_text_box(self):
        return self.wait_url_contains("text-box")