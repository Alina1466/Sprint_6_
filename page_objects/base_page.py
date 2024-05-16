import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем объект {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на ')
    def click(self, locator):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Печатаем текст в поле ввода')
    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст из локатора')
    def get_text_element(self, locator):
        self.wait_element(locator)
        return locator.text

    @allure.step('Скроллим к локатору {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание открытия нового окна в браузере')
    def wait_until_new_window_is_open(self, driver, urls):
        WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(expected_conditions.url_contains(urls))

    @allure.step('Кликнуть на элемент {locator}')
    def click_on_element(self, locator):
        element = self.wait_element(locator)
        element.click()



