from selenium.webdriver.common.by import By


class PageOrderLocators:

    order_title = (By.CLASS_NAME, 'Order_Header__BZXOb') # Заголовок на странице оформления заказа самоката
    header_order_btn = (By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]') # Кнопка 'Заказать' в шапке
    lower_order_btn = (By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]') # Кнопка "Заказать" внизу главной страницы
    input_name = (By.XPATH, './/input[@placeholder="* Имя"]') # Поле ввода имени на странице оформления заказа
    input_surname = (By.XPATH, './/input[@placeholder="* Фамилия"]') # Поле ввода фамилии на странице оформления заказа
    input_adress = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле ввода адреса, куда привезти заказ
    drop_list_metro = (By.CLASS_NAME, "select-search__input") # Выпадающий список станций метро на странице оформелния заказа
    metro_station_item = (By.XPATH, '//div[text()="Калужская"]') # Станиция метро 'Калужская'
    input_phone_number = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле ввода номера телефона на который позвонит курьер
    next_btn = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM') # Кнопка 'Далее' на странице оформления заказа
    rent_title = (By.XPATH, '//div[text()="Про аренду"]') # Заголовок 'Про аренду' на страничке оформления заказа
    input_day_rent_start = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]') # Поле ввода даты, когда привезти самокат
    date_picker_rent_start = (By.CLASS_NAME, 'react-datepicker-popper') # Календарь для ввода даты, когда нужно привезти самокат
    date_rent_list = (By.XPATH, '//div[text() = "* Срок аренды"]') # Кнопка выпадающего спиcка для срока аренды
    three_days_rent_el = (By.XPATH, './/div[@class = "Dropdown-option" and text()="трое суток"]') # Вариант ""трое суток"" аренды из выпадающего списка
    grey_checkbox = (By.ID, "grey") # Чекбокс выбора серого цвета арендуемых самокатов
    input_courier_comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # Поле ввода комментария для курьера
    order_btn = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]') # Кнопка "Заказать" на страничке оформления заказа
    modal_order_window = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ') # Всплывающее окно подтверждения оформления заказа
    yes_btn_in_modal = (By.XPATH, './/button[text()="Да"]') # Кнопка "ДА" подтверждения оформления заказа во всплывающем окне
    order_completed_modal = (By.XPATH, './/*[contains(@class,"Order_ModalHeader")]') # Сообщение о заказе во всплывающем окне
    block_order_info = (By.XPATH, '//div[contains(@class, "Order_Content")]') # Блок оформления заказа с полями для ввода личных данных