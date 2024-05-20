from selenium.webdriver.common.by import By
class HomePageLocators:

    HOME_SUBTITLE = [By.XPATH, '(.//div[contains(@id,"accordion__heading-")])[last()]']  # Подзаголовок 'Вопросы о важном'
    HOME_TITLE = (By.CLASS_NAME, 'Home_Header__iJKdX')  # Заголовок на главной странице
    CELL_QUESTION = (By.ID, 'accordion__heading-{}')  # Локатор вопросов без индекса
    CELL_ANSWER = (By.ID, "accordion__panel-{}")  # Локатор ответов без индекса
    COCOKIES_BTN = (By.ID, 'rcc-confirm-button')  # Кнопка "Да все привыкли" в куках на главной странице
    HEADER_STATUS_ORDER_BTN = (By.CLASS_NAME, 'Header_Link__1TAG7') # Кнопка 'Статус заказа' в шапке
    HEADER_INPUT_NUM_ORDER = (By.CLASS_NAME, 'Input_Input__1iN_Z.Header_Input__xIoUq') # Поле ввода для номера заказа в шапке
    HEADER_SEARCH_BTN_STATUS = (By.CLASS_NAME, 'Button_Button__ra12g.Header_Button__28dPO') # Кнопка 'GO' для выполнения поиска по номеру заказа
