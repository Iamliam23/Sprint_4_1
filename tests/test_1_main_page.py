from pages.main_page import MainPageQaScooter



class TestMainPageQaScooter():
    def test_questions_important_1_waitfor_correct_header_1(self, driver, get_the_page, go_to_questions_important):
        main_page_qa_sc = MainPageQaScooter(driver)
        main_page_qa_sc.check_element_1()
        main_page_qa_sc.check_element_2()
        main_page_qa_sc.check_element_3()
        main_page_qa_sc.check_element_4()
        main_page_qa_sc.check_element_5()
        main_page_qa_sc.check_element_6()
        main_page_qa_sc.check_element_7()
        main_page_qa_sc.check_element_8()


