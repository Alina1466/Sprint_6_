from selenium.webdriver.common.by import By


class PageOrderLocators:

    ORDER_TITLE = (By.CLASS_NAME, 'Order_Header__BZXOb') # Заголовок на странице оформления заказа самоката
    INPUT_NAME = (By.XPATH, './/input[@placeholder="* Имя"]') # Поле ввода имени на странице оформления заказа
    INPUT_SURNAME = (By.XPATH, './/input[@placeholder="* Фамилия"]') # Поле ввода фамилии на странице оформления заказа
    INPUT_ADRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле ввода адреса, куда привезти заказ
    DROP_LIST_METRO = (By.CLASS_NAME, "select-search__input") # Выпадающий список станций метро на странице оформелния заказа
    METRO_STATION_ITEM = (By.XPATH, '//div[text()="Калужская"]') # Станиция метро 'Калужская'
    INPUT_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле ввода номера телефона на который позвонит курьер
    NEXT_BTN = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM') # Кнопка 'Далее' на странице оформления заказа
    RENT_TITLE = (By.XPATH, '//div[text()="Про аренду"]') # Заголовок 'Про аренду' на страничке оформления заказа
    INPUT_DAY_RENT_START = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]') # Поле ввода даты, когда привезти самокат
    DATE_PICKER_RENT_START = (By.CLASS_NAME, 'react-datepicker-popper') # Календарь для ввода даты, когда нужно привезти самокат
    DATE_RENT_LIST = (By.XPATH, '//div[text() = "* Срок аренды"]') # Кнопка выпадающего спиcка для срока аренды
    THREE_DAYS_RENT_EL = (By.XPATH, './/div[@class = "Dropdown-option" and text()="трое суток"]') # Вариант ""трое суток"" аренды из выпадающего списка
    GREY_CHECKBOX = (By.ID, "grey") # Чекбокс выбора серого цвета арендуемых самокатов
    INPUT_COURIER_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # Поле ввода комментария для курьера
    ORDER_BTN = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]') # Кнопка "Заказать" на страничке оформления заказа
    MODAL_ORDER_WINDOW = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ') # Всплывающее окно подтверждения оформления заказа
    YES_BTN_IN_MODAL = (By.XPATH, './/button[text()="Да"]') # Кнопка "ДА" подтверждения оформления заказа во всплывающем окне
    ORDER_COMPLETED_MODAL = (By.XPATH, './/*[contains(@class,"Order_ModalHeader")]') # Сообщение о заказе во всплывающем окне
    BLOCK_ORDER_INFO = (By.XPATH, '//div[contains(@class, "Order_Content")]') # Блок оформления заказа с полями для ввода личных данных
    SCOOTER_SAMOKAT = (By.CLASS_NAME, 'class="Header_LogoScooter__3lsAR"')  # Логотип Самоката на главной странице
    HEADER_ORDER_BTN = (By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]') # Кнопка 'Заказать' в шапке
    LOWER_ORDER_BTN = (By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]') # Кнопка "Заказать" внизу главной страницы