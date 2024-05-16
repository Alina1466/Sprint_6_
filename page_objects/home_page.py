import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    home_subtitle = (By.XPATH,'//div[@class="Home_SubHeader__zwi_E" and contains(text(), "Вопросы о важном")]')  # Подзаголовок 'Вопросы о важном'
    home_title = (By.CLASS_NAME, 'Home_Header__iJKdX')  # Заголовок на главной странице
    cell_question = (By.ID, 'accordion__heading-{}')  # Локатор вопросов без индекса
    cell_answer = (By.ID, "accordion__panel-{}")  # Локатор ответов без индекса
    cocokies_btn = (By.ID, 'rcc-confirm-button')  # Кнопка "Да все привыкли" в куках на главной странице

    @allure.step('Ждем кнопку кук и кликаем на неё')
    def click_cookie_button(self):
        self.click(HomePage.cocokies_btn)


    @allure.step('Кликаем на вопрос в аккордеоне')
    def tap_question(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем в открывшемся элементе аккордеона ответ на вопрос')
    def find_answer(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text

