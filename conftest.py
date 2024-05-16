import pytest
from selenium import webdriver
from url_s import URL

@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get(URL.main)
    yield browser
    browser.quit()