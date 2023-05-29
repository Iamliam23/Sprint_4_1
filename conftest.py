from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators


@pytest.fixture()
def get_driver_and_page():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture()
def go_to_questions_important(get_driver_and_page):

    get_driver_and_page.find_element(*Locators.SCOOTER_COOP_DAYS_HEADER)

    cookie = get_driver_and_page.find_element(*Locators.COOKIE_ELEMENT)
    cookie.click()

    questions_header = get_driver_and_page.find_element(*Locators.QUESTIONS_IMPORTANT)
    get_driver_and_page.execute_script("arguments[0].scrollIntoView();", questions_header)
@pytest.fixture()
def go_to_registration_page(get_driver_and_page):

    cookie = get_driver_and_page.find_element(*Locators.COOKIE_ELEMENT)
    cookie.click()

    order_but_2 = WebDriverWait(get_driver_and_page, 5).until(EC.presence_of_element_located((Locators.ORDER_BUTTON_1)))
    order_but_2.click()








