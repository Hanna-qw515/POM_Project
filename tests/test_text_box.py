# tests/test_text_box.py
from pages.text_box_page import TextBoxPage


def test_submit_full_form(driver):              # driver придёт из conftest.py
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form("Ivan Tester", "ivan@test.com", "Praha, Vodičkova 1", "Brno, Masarykova 2")
    page.submit()

    assert "Ivan Tester" in page.get_output_name()
    assert "ivan@test.com" in page.get_output_email()
    assert "Praha, Vodičkova 1" in page.get_output_current_address()
    assert "Brno, Masarykova 2" in page.get_output_permanent_address()


def test_invalid_email_is_highlighted(driver):
    page = TextBoxPage(driver)
    page.open_page()
    page.fill_form(full_name="Ivan Tester", email="ivan.tester")   # нет @ и домена
    page.submit()
    assert page.is_email_marked_invalid(), "Поле email не подсветилось красным"
    assert not page.is_output_shown(), "Форма с невалидным email не должна отправляться"
