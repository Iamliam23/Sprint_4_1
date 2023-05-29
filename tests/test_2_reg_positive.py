from pages.reg_positive import RegistrationPositive
from pages.base_page import BasePageMethods



class TestRegistrationPositive():

    def test_registration_correct_inputs_no_errors_success_order(self, driver, get_the_page):
        BasePageMethods(driver).click_order_but_1()
        BasePageMethods(driver).wait_for_whom_header()
        BasePageMethods(driver).click_cookie()
        RegistrationPositive(driver).set_inputs_correct()
        RegistrationPositive(driver).click_further_but()
        BasePageMethods(driver).wait_rent_header()
        RegistrationPositive(driver).set_inputs_correct_2()
        RegistrationPositive(driver).make_order()



