
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    print('Запуск браузера...')
    options = Options()
    options.page_load_strategy = 'eager'  # Set the page load strategy to 'eager'
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()

    yield browser

    print('Закрытие браузера...')
    browser.quit()
