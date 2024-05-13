import allure

from locators.header_page_locators import HeaderPageLocators
from page_objects.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу Яндекса в шапке страницы')
    def click_on_yandex_logo(self):
        self.click(HeaderPageLocators.logo_yandex_header)

    @allure.step('Клик по логотипу "Самоката" в шапке страницы')
    def click_on_scooter_logo(self):
        self.click(HeaderPageLocators.logo_scooter_header)

    def click_logo_yandex_header(self):
        pass