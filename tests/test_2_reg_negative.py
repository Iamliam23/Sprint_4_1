from pages.reg_negative import RegistrationNegative
from pages.base_page import BasePageMethods




class TestRegistrationNegative():

    def test_registration_incorrect_inputs_errors_appears_success_order(self, driver, get_the_page):
        BasePageMethods(driver).click_order_but_1()
        BasePageMethods(driver).wait_for_whom_header()
        BasePageMethods(driver).click_cookie()
        RegistrationNegative(driver).set_inputs_incorrect()
        RegistrationNegative(driver).set_inputs_correct()
        RegistrationNegative(driver).click_further_but()
        BasePageMethods(driver).wait_rent_header()
        RegistrationNegative(driver).set_inputs_incorrect_2()
        RegistrationNegative(driver).make_order()



