import allure
import pytest
from user_data import Info
from page_objects.home_page import HomePage
from conftest import driver


class TestDropDownList:
    @allure.title('Тест открытия ответов на главной странице "Вопросы о важном"')
    @allure.description('Клик по вопросам по очереди, нажимая на стрелку - открываются ответы на вопросы')
    @pytest.mark.parametrize("index, text_of_answer", Info.answers,)

    def test_faq(self, driver, index, text_of_answer):
        home_page = HomePage(driver)
        home_page.click_cookie_button()
        home_page.scroll_to_element()
        home_page.click_question(index)

        assert home_page.get_answer(index) == text_of_answer