from pages.elements_page import TextBoxPage

def test_wait_url_contains(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.text_button()
    assert page.wait_url_contains_text_box()
