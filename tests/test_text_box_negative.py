import pytest
from pages.text_box_page import TextBoxPage


@pytest.mark.parametrize(
    "email, should_be_invalid, should_show_output, case_name",
    [
        ("ivan.tester.com", True, False, "Email без @"),
        ("ivan@", True, False, "Email без части после @"),
        ("ivan @test.com", True, False, "Email с пробелом"),
        ("ivan@test", True, False, "Email без доменной зоны"),
        ("", False, False, "Пустая форма"),
    ]
)
def test_text_box_email_validation(driver, email, should_be_invalid, should_show_output, case_name):
    page = TextBoxPage(driver)
    page.open_page()

    if email:
        page.fill_form(full_name="Ivan Tester", email=email)

    page.submit()

    assert page.is_email_marked_invalid() == should_be_invalid, f"{case_name}: неправильная подсветка email"
    assert page.is_output_shown() == should_show_output, f"{case_name}: неверное отображение блока результата"
