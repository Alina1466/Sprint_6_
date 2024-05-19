import allure
from page_objects.header_page import HeaderPage
from conftest import driver
from url_s import URL


class TestClickLogo:
    @allure.title('тест проверки перехода на другую страницу кликом по логотипу.')
    @allure.description(
        'проверяем то, что если кликнуть на логотип Яндекса - в новом окне через редирект откроется главная '
        'страница Дзена.')
    def test_check_working_yandex_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_on_yandex_logo()
        header_page.tab_switch(driver)
        header_page.check_redirection_on_dzen_page()
        assert header_page.get_current_url() == URL.dzen_page_url


    @allure.title('Тест проверки редиректа на главную страницу кликом на логотип "Самоката"')
    @allure.description(
        'Проверяем то, что если кликнуть на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_check_working_scooter_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_on_scooter_logo()
        header_page.check_redirection_on_scooter_page()
        assert header_page.get_current_url() == URL.scooter_page_url
