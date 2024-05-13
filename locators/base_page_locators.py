from selenium.webdriver.common.by import By


class BasePageLocators:

    header_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR') # Логотип самоката в шапке страницы
    cocokies_btn = (By.ID, 'rcc-confirm-button') # Кнопка "Да все привыкли" в куках на главной странице
    header_status_order_btn = (By.CLASS_NAME, 'Header_Link__1TAG7') # Кнопка 'Статус заказа' в шапке
    header_input_num_order = (By.CLASS_NAME, 'Input_Input__1iN_Z.Header_Input__xIoUq') # Поле ввода для номера заказа в шапке
    header_search_btn_status = (By.CLASS_NAME, 'Button_Button__ra12g.Header_Button__28dPO') # Кнопка 'GO' для выполнения поиска по номеру заказа