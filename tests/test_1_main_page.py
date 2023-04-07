from pages.main_page import MainPageQaScooter



class TestMainPageQaScooter():
    def test_questions_important_1_waitfor_correct_header_1(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_1()
        MainPageQaScooter(driver).check_element_2()
        MainPageQaScooter(driver).check_element_3()
        MainPageQaScooter(driver).check_element_4()
        MainPageQaScooter(driver).check_element_5()
        MainPageQaScooter(driver).check_element_6()
        MainPageQaScooter(driver).check_element_7()
        MainPageQaScooter(driver).check_element_8()


