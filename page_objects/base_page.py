import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем объект {locator}')
    def find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на ')
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Печатаем текст в поле ввода')
    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Ожидание')
    def cross_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))


    @allure.step('Поиск элемента в новом окне')
    def tab_switch(self, driver):
        self.driver.switch_to.window(driver.window_handles[1])


    @allure.step('Сравнение url')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Клик на {locator}')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Текст')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скроллим к локатору')
    def scroll_to_element(self,):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

