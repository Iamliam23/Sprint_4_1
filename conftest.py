from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def get_the_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    return driver



