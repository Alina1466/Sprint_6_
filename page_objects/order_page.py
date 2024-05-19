import random
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locators.order_page_locators import PageOrderLocators


class OrderPage(BasePage):
    @allure.step('Кликаем на кнопку Заказать в шапке страницы')
    def click_order_header_btn(self):
        self.click(PageOrderLocators.HEADER_ORDER_BTN)

    @allure.step('Кликаем на кнопку Заказть в подвале страницы')
    def click_order_lower_btn(self):
        self.click(PageOrderLocators.LOWER_ORDER_BTN)

    @allure.step('Вводим Имя')
    def input_name(self, name):
        self.input_text(PageOrderLocators.INPUT_NAME, name)

    @allure.step('Вводим Фамилию')
    def input_surname(self, surname):
        self.input_text(PageOrderLocators.INPUT_SURNAME, surname)

    @allure.step('Добавляем адрес')
    def input_address(self, address):
        self.input_text(PageOrderLocators.INPUT_ADRESS, address)

    @allure.step('Вписываем метро')
    def choice_metro(self, metro):
        self.click(PageOrderLocators.DROP_LIST_METRO)
        self.input_text(PageOrderLocators.DROP_LIST_METRO, metro)
        self.click(PageOrderLocators.METRO_STATION_ITEM)

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, number):
        self.input_text(PageOrderLocators.INPUT_PHONE_NUMBER, number)

    @allure.step('Генерируем случайную дату и вводим ее')
    def input_start_date_rent(self):
        date = str(random.randint(10, 28)) + '.' + str(random.randint(10, 12)) + '.2024'
        self.input_text(PageOrderLocators.INPUT_DAY_RENT_START, date)
        self.click(PageOrderLocators.RENT_TITLE)

    @allure.step('Выбираем срок аренды')
    def order_filled_date(self):
        self.click(PageOrderLocators.DATE_RENT_LIST)
        self.click(PageOrderLocators.THREE_DAYS_RENT_EL)

    @allure.step('Вписываем пользовательские данные для оформления заказа')
    def filling_personal_date_action(self, name, surname, address, metro, number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choice_metro(metro)
        self.input_phone_number(number)
        self.click(PageOrderLocators.NEXT_BTN)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PageOrderLocators.RENT_TITLE))
        self.input_start_date_rent()
        self.order_filled_date()
        self.click(PageOrderLocators.GREY_CHECKBOX)
        self.input_text(PageOrderLocators.INPUT_COURIER_COMMENT, 'Fus-Ro-Dah!!!!')
        self.click(PageOrderLocators.ORDER_BTN)
        self.click(PageOrderLocators.YES_BTN_IN_MODAL)

    @allure.step('Ждем появления окна подтверждения заказа')
    def check_congratulation_modal(self):
        locator = self.find_element(PageOrderLocators.ORDER_COMPLETED_MODAL)
        return locator.text


