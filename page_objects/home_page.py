import allure
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    @allure.step('Ждем кнопку кук и кликаем на неё')
    def click_cookie_button(self):
        self.find_element(HomePageLocators.COCOKIES_BTN)
        self.click(HomePageLocators.COCOKIES_BTN)

   # @allure.step('Скроллим к локатору')
    #def scroll_to_element(self,):
     #   self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    @allure.step('Нажать на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.CELL_QUESTION
        locator = locator.format(number)
        return self.click_on_element((method, locator))

    @allure.step('Получить текст ответа на вопрос')
    def get_answer(self, number):
        method, locator = HomePageLocators.CELL_ANSWER
        locator = locator.format(number)
        return self.get_text((method, locator))
