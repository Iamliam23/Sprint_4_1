from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait



class BasePageMethods():

    def __init__(self, driver):
        self.driver = driver

    def wait_main_page(self):
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.SCOOTER_COOP_DAYS_HEADER)))

    def click_order_but_1(self):
        order_but_1 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.ORDER_BUTTON_1)))
        order_but_1.click()

    def click_order_but_2(self):
        order_but_2 = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.ORDER_BUTTON_2)))
        order_but_2.click()

    def wait_for_whom_header(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.FOR_WHOM_ELEMENT)))

    def click_cookie(self):
        cookie = self.driver.find_element(*Locators.COOKIE_ELEMENT)
        cookie.click()

    def wait_rent_header(self):
        rent_header = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((Locators.ABOUT_RENT_HEADER)))
        assert rent_header.is_displayed()
