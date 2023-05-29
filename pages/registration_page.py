from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from data import Answers
import random



class Registration:
    def __init__(self, driver):
        self.driver = driver

    def click_scooter_link(self):
        scooter_but = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((Locators.SCOOTER_BUTTON)))
        scooter_but.click()

    def wait_for_whom_header(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.FOR_WHOM_ELEMENT)))

    def set_name_input_incorrect(self):
        name_input = self.driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(Answers.name_incorrect)
        surname_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.SURNAME_INPUT)))
        surname_input.click()

    def set_surname_input_incorrect(self):
        surname_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Locators.SURNAME_INPUT)))
        surname_input.send_keys(Answers.surname_incorrect)
        address_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Locators.ADDRESS_INPUT)))
        address_input.click()

    def set_address_input_incorrect(self):
        address_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.ADDRESS_INPUT)))
        address_input.send_keys(Answers.address_incorrect)
        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Locators.PHONE_INPUT)))
        phone_input.click()

    def set_phone_input_incorrect(self):
        phone_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.PHONE_INPUT)))
        phone_input.send_keys(Answers.phone_incorrect)
        empty_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.EMPTY_FIELD)))
        empty_field.click()

    def check_metro_input_incorrect(self):
        further_but = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((Locators.FURTHER_BUTTON)))
        further_but.click()

    def set_inputs_incorrect(self):
        self.set_name_input_incorrect()
        self.set_surname_input_incorrect()
        self.set_address_input_incorrect()
        self.set_phone_input_incorrect()
        self.check_metro_input_incorrect()

    def set_name_input(self):
        self.driver.find_element(*Locators.NAME_INPUT).clear()
        self.driver.find_element(*Locators.NAME_INPUT).send_keys(Answers.name_correct)

    def set_surname_input(self):
        self.driver.find_element(*Locators.SURNAME_INPUT).clear()
        self.driver.find_element(*Locators.SURNAME_INPUT).send_keys(Answers.surname_correct)

    def set_address_input(self):
        self.driver.find_element(*Locators.ADDRESS_INPUT).clear()
        self.driver.find_element(*Locators.ADDRESS_INPUT).send_keys(Answers.address_correct)

    def select_metro_station(self):
        metro_st_input = self.driver.find_element(*Locators.METRO_STATION_INPUT)
        metro_st_input.click()
        list_items = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.METRO_STATION_UL_2)))
        element_x = random.choice(list_items)
        element_x.click()

    def set_phone_numb(self):
        phone_input = self.driver.find_element(*Locators.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(Answers.phone_correct)

    def set_inputs_correct(self):
        self.set_name_input()
        self.set_surname_input()
        self.set_address_input()
        self.select_metro_station()
        self.set_phone_numb()

    def click_further_but(self):
        further_but = self.driver.find_element(*Locators.FURTHER_BUTTON)
        further_but.click()

    def wait_rent_header(self):
        rent_header = self.driver.find_element(*Locators.ABOUT_RENT_HEADER)
        assert rent_header.is_displayed()

    def select_delivery_date_incorrect(self):
        delivery_date = self.driver.find_element(*Locators.SELECT_DELIVERY_DATE)
        delivery_date.click()
        past_date = self.driver.find_element(*Locators.SELECT_PAST_DATE)
        past_date.click()
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
        comment_input.send_keys(Answers.comment)

    def set_inputs_incorrect_2(self):
        self.select_delivery_date_incorrect()
        self.select_rental_period()
        self.select_scooter_color()
        self.write_comment()

    def select_delivery_date_correct(self):
        delivery_date = self.driver.find_element(*Locators.SELECT_DELIVERY_DATE)
        delivery_date.click()
        div_options_2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Locators.SELECT_FUTURE_DATE)))
        div_options_2.click()

    def set_inputs_correct_2(self):
        self.select_delivery_date_correct()
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
    def make_order_2(self):
        order_but_3 = self.driver.find_element(*Locators.ORDER_BUTTON_3)
        order_but_3.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((Locators.PLACE_ORDER_HEADER)))
        yes_but = self.driver.find_element(*Locators.YES_BUTTON)
        yes_but.click()
        status_but = self.driver.find_element(*Locators.SEE_STATUS_BUTTON)
        status_but.click()





















