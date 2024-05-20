import allure
from locators.header_page_locators import HeaderPageLocators
from page_objects.base_page import BasePage
from url_s import URL


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу Яндекса в шапке страницы')
    def click_on_yandex_logo(self):
        self.click(HeaderPageLocators.LOGO_YANDEX_HEADER)

    @allure.step('Клик по логотипу "Самоката" в шапке страницы')
    def click_on_scooter_logo(self):
        self.click(HeaderPageLocators.LOGO_SCOOTER_HEADER)

    @allure.step('Проверить URL "Дзен"')
    def check_redirection_on_dzen_page(self):
        self.cross_url(URL.dzen_page_url)

    @allure.step('Проверить URL "Яндекс Самокат"')
    def check_redirection_on_scooter_page(self):
        self.cross_url(URL.scooter_page_url)