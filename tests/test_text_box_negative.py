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
    page.submit()
    assert not page.is_email_marked_invalid(),"Поле email не подсветилось красным"
    assert not page.is_output_shown(),"Форма с невалидным email не должна отправляться"
