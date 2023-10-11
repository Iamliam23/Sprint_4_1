import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import Registration
from locators.locators import Locators




class TestRegistrationNegative:

    @pytest.mark.parametrize("the_error",[Locators.NAME_ERROR, Locators.SURNAME_ERROR, Locators.ADDRESS_ERROR, Locators.PHONE_ERROR, Locators.METRO_STATION_ERROR])
    def test_registration_incorrect_inputs_errors_appears_1(self, get_driver_and_page, go_to_registration_page, the_error):
        reg_negative_1 = Registration(get_driver_and_page)
        reg_negative_1.wait_for_whom_header()
        reg_negative_1.set_inputs_incorrect()
        error = WebDriverWait(get_driver_and_page, 10).until(EC.visibility_of_element_located((the_error)))
        assert error.is_displayed()

    @pytest.mark.parametrize("the_error_2",[Locators.ORDER_STATUS_ERROR])
    def test_registration_incorrect_inputs_errors_appears_2(self, get_driver_and_page, go_to_registration_page,the_error_2):
        reg_negative_2 = Registration(get_driver_and_page)
        reg_negative_2.set_inputs_correct()
        reg_negative_2.click_further_but()
        reg_negative_2.wait_rent_header()
        reg_negative_2.set_inputs_incorrect_2()
        reg_negative_2.make_order()
        order_st_error = WebDriverWait(get_driver_and_page, 10).until(EC.presence_of_element_located((the_error_2)))
        assert order_st_error.text == "Не успеем привезти самокат вовремя. Чтобы уточнить статус заказа, позвоните в поддержку: 0101"

