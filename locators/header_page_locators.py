from selenium.webdriver.common.by import By


class HeaderPageLocators:

    LOGO_YANDEX_HEADER = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]' # Логотип Яндекса на главной странице
    LOGO_SCOOTER_HEADER = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]' # Логотип Самоката на главной странице