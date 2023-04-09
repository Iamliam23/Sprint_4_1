import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from pages.main_page import MainPageQaScooter
from pages.main_page_2 import MainPageQaScooter



class TestMainPageQaScooter:

    def test_questions_important_waitfor_correct_header_1(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_1()
        qu_header_1 = MainPageQaScooter(driver).question_header_1()
        actually_value = qu_header_1.text
        expected_value = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert actually_value == expected_value, f"Заголовок вопроса 1 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_2(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_2()
        qu_header_2 = MainPageQaScooter(driver).question_header_2()
        actually_value = qu_header_2.text
        expected_value = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert actually_value == expected_value, f"Заголовок вопроса 2 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_3(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_3()
        qu_header_3 = MainPageQaScooter(driver).question_header_3()
        actually_value = qu_header_3.text
        expected_value = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert actually_value == expected_value, f"Заголовок вопроса 3 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_4(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_4()
        qu_header_4 = MainPageQaScooter(driver).question_header_4()
        actually_value = qu_header_4.text
        expected_value = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert actually_value == expected_value, f"Заголовок вопроса 4 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_5(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_5()
        qu_header_5 = MainPageQaScooter(driver).question_header_5()
        actually_value = qu_header_5.text
        expected_value = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert actually_value == expected_value, f"Заголовок вопроса 5 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_6(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_6()
        qu_header_6 = MainPageQaScooter(driver).question_header_6()
        actually_value = qu_header_6.text
        expected_value = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert actually_value == expected_value, f"Заголовок вопроса 6 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_7(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_7()
        qu_header_7 = MainPageQaScooter(driver).question_header_7()
        actually_value = qu_header_7.text
        expected_value = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert actually_value == expected_value, f"Заголовок вопроса 7 должен быть '{expected_value}', но было '{actually_value}'"
    def test_questions_important_waitfor_correct_header_8(self, driver, get_the_page, go_to_questions_important):
        MainPageQaScooter(driver).check_element_8()
        qu_header_8 = MainPageQaScooter(driver).question_header_8()
        actually_value = qu_header_8.text
        expected_value = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        assert actually_value == expected_value, f"Заголовок вопроса 8 должен быть '{expected_value}', но было '{actually_value}'"



