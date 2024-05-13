from selenium.webdriver.common.by import By


class HomeLocators:

    home_title = (By.CLASS_NAME, 'Home_Header__iJKdX') # Заголовок на главной странице
    home_subtitle = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E" and contains(text(), "Вопросы о важном")]') # Подзаголовок 'Вопросы о важном'
    cell_question = (By.ID, 'accordion__heading-{}') # Локатор вопросов без индекса
    cell_answer = (By.ID, "accordion__panel-{}") # Локатор ответов без индекса