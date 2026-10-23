from pages.radio_button_page import RadioButtonPage

def test_choose_yes(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.choose_yes()
    assert "Yes" in page.get_result(), "После выбора Yes результат не появился"

def test_switch_from_yes_to_impressive(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    page.choose_impressive()
    assert "Impressive" in page.get_result(), "После переключения на Impressive результат неверный"

def test_no_radio_button_is_disabled(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    assert page.is_no_enabled() is False, "Radio button No не должен быть активным"
def test_list_elements_buttons(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    assert page.list_elements_buttons() == ["Yes", "Impressive","No"]

def test_title_page(driver):
    page = RadioButtonPage(driver)
    page.open_page()
    assert "DEMOSITE" in page.title_page().upper()