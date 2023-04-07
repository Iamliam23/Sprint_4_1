from selenium import webdriver
import pytest
from locators.locators import Locators


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def get_the_page(driver):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    return driver

@pytest.fixture()
def go_to_questions_important(driver):
    driver.find_element(*Locators.SCOOTER_COOP_DAYS_HEADER)

    cookie = driver.find_element(*Locators.COOKIE_ELEMENT)
    cookie.click()

    questions_header = driver.find_element(*Locators.QUESTIONS_IMPORTANT)
    driver.execute_script("arguments[0].scrollIntoView();", questions_header)




