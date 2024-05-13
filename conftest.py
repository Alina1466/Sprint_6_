import pytest
from selenium import webdriver
from URLs import URL

@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get(URL.main)
    yield browser
    browser.quit()