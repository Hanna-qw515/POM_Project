from pages.dynamic_properties_page import DynamicPropertiesPage

def test_activation_after_inactivity_period(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert not page.is_enable_after_button_enabled(),'Кнопка активна'
    assert page.wait_until_button_enabled(),'Кнопка заблокирована'
def test_is_color_changed(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert page.is_color_changed(),'Кнопка не меняет цвет текста'
def test_is_visible_after_button_shown(driver):
    page = DynamicPropertiesPage(driver)
    page.open_page()
    assert page.is_visible_after_button_shown(),'Кнопка не появилась'