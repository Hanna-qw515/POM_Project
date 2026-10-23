from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class DynamicPropertiesPage(BasePage):
    URL = "https://demoqa.com/dynamic-properties"
    WILL_ENABLE = (By.ID,"enableAfter")
    COLOR_CHANGE = (By.ID,"colorChange")
    VISIBLE_AFTER = (By.ID,"visibleAfter")

    def open_page(self):
        self.open(self.URL)

    def is_enable_after_button_enabled(self):
        return self.driver.find_element(*self.WILL_ENABLE).is_enabled()


    def wait_until_button_enabled(self):
        return self.wait_clickable(self.WILL_ENABLE)

    def is_color_changed(self):
        return self.has_class(self.COLOR_CHANGE,"text-danger", timeout=7)

    def is_visible_after_button_shown(self):
        return self.is_visible(self.VISIBLE_AFTER, timeout=7)





