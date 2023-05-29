from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePageMethods
from locators.locators import Locators
import random



class RegistrationPositive(BasePageMethods):

    def set_name_input(self):
        self.driver.find_element(*Locators.NAME_INPUT).send_keys("Юрий")

    def set_surname_input(self):
        self.driver.find_element(*Locators.SURNAME_INPUT).send_keys("Имптев")

    def set_address_input(self):
        self.driver.find_element(*Locators.ADDRESS_INPUT).send_keys("Кореновская")

    def select_metro_station(self):
        metro_st_input = self.driver.find_element(By.CLASS_NAME, "select-search__input")
        metro_st_input.click()
        list_items = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.METRO_STATION_UL_2)))
        element_x = random.choice(list_items)
        element_x.click()
        assert metro_st_input.get_attribute('value') != "", "Element has no text value"

    def set_phone_numb(self):
        self.driver.find_element(*Locators.PHONE_INPUT).send_keys("+79602746342")

    def set_inputs_correct(self):
        self.set_name_input()
        self.set_surname_input()
        self.set_address_input()
        self.select_metro_station()
        self.set_phone_numb()

    def click_further_but(self):
        further_but = self.driver.find_element(*Locators.FURTHER_BUTTON)
        further_but.click()

    def select_delivery_date(self):
        delivery_date = self.driver.find_element(*Locators.SELECT_DELIVERY_DATE)
        delivery_date.click()
        div_buttons = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.DIV_BUTTONS)))
        element_x = random.choice(div_buttons)
        element_x.click()
        assert delivery_date.get_attribute('value') != "", "Element has no text value"

    def select_rental_period(self):
        rent_period = self.driver.find_element(*Locators.SELECT_RENTAL_PERIOD)
        rent_period.click()
        div_options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.SELECT_RENTAL_PERIOD_2)))
        element_z = random.choice(div_options)
        element_z.click()
        assert rent_period.get_attribute('value') != "", "Element has no text value"

    def select_scooter_color(self):
        scooter_colors = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.SCOOTER_COLORS)))
        element_u = random.choice(scooter_colors)
        element_u.click()

    def write_comment(self):
        comment_input = self.driver.find_element(*Locators.COMMENT_INPUT)
        comment_input.send_keys("Привет, курьер!")

    def set_inputs_correct_2(self):
        self.select_delivery_date()
        self.select_rental_period()
        self.select_scooter_color()
        self.write_comment()

    def make_order(self):
        order_but_3 = self.driver.find_element(*Locators.ORDER_BUTTON_3)
        order_but_3.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.PLACE_ORDER_HEADER)))
        yes_but = self.driver.find_element(*Locators.YES_BUTTON)
        yes_but.click()
        status_but = self.driver.find_element(*Locators.SEE_STATUS_BUTTON)
        status_but.click()
        assert 'https://qa-scooter.praktikum-services.ru/track?t' in self.driver.current_url























