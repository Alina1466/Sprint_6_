# Sprint_6_

Название проекта: Sprint_6

Проект содержит в себе папку с тестами - tests, директорию локаторов - locators, файл с фикстурами - conftest.py, используемые URL вынесены в отдельный файл URLs.py, файл .gitignor, папку allure_results с отчётом о проекте

Описание проекта:

- Файл "test_dropdown_list.py" - Проверяем работу выпадающего списка в разделе «Вопросы о важном» на главной странице. При клике на стрелочку, открывается соответствующий текст.
- Файл "test_order_scooter.py" - Проверяем заказ самоката с двумя наборами данных
- Файл "test_click_logo.py" - Проверяем, что при клике на "Яндекс" - открывается редирект в главной страницей Дзена. И второй тест, что при клике на надпись "Самокат" - осущеставляется переход на главную страницу самоката

Папка allure_results - содержит отчёт о проекте
Директория locators - содержит 4 файла в которых описаны локаторы, используемые в кодах при написании проекта
Файл conftest.py - содержит фикстуру
Файл url_s.py - содержит URLы, которые используются в кодах
Файл user_data.py - содержит в себе ответы на вопросы, которые описаны в "Вопросы о важном" и персональные данные, которые состоят из 2 наборов
Директория page_object - содержит 4 файла