import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import Registration
from locators.locators import Locators



class TestRegistrationPositive:

    @pytest.mark.parametrize("the_error_3", [Locators.ORDER_STATUS_ERROR])
    def test_registration_correct_inputs_no_errors_success_order(self, get_driver_and_page, go_to_registration_page, the_error_3):
        reg_positive = Registration(get_driver_and_page)
        reg_positive.wait_for_whom_header()
        reg_positive.set_inputs_correct()
        reg_positive.click_further_but()
        reg_positive.wait_rent_header()
        reg_positive.set_inputs_correct_2()
        reg_positive.make_order_2()
        order_st_error_2 = WebDriverWait(get_driver_and_page, 10).until(EC.presence_of_element_located((the_error_3)))
        assert order_st_error_2.text == "Скоро курьер заберет его"




