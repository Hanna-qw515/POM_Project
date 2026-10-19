from pages.radio_button_page import RadioButtonPage

def test_choose_yes(browser):
    page = RadioButtonPage(browser)
    page.open_page()
    page.choose_yes()
    assert "Yes" in page.get_result(), "После выбора Yes результат не появился"

def test_switch_from_yes_to_impressive(browser):
    page = RadioButtonPage(browser)
    page.open_page()
    page.choose_impressive()
    assert "Impressive" in page.get_result(), "После переключения на Impressive результат неверный"

def test_no_radio_button_is_disabled(browser):
    page = RadioButtonPage(browser)
    page.open_page()
    assert page.is_no_enabled() is False, "Radio button No не должен быть активным"
