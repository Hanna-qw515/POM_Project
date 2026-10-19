# pages/base_page.py
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)
        self.remove_ads()

    def remove_ads(self):
        self.driver.execute_script(
            "document.querySelectorAll('#fixedban, footer').forEach(el => el.remove());"
        )

    def find(self, locator):
        return  self.wait.until((EC.presence_of_element_located(locator)))

    def is_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def has_class(self, locator, class_name, timeout=3):
        # Ждём, пока в атрибуте class появится нужное значение (например, "field-error")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element_attribute(locator, "class", class_name)
            )
            return True
        except TimeoutException:
            return False