from selenium.webdriver.common.by import By


class HeaderPageLocators:

    logo_yandex_header = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]' # Логотип Яндекса на главной странице
    logo_scooter_header = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]' # Логотип Самоката на главной странице