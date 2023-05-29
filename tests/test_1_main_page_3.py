import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators



class TestMainPageQaScooter:
    @pytest.mark.parametrize("the_question, question_header, expected_value",
        [(Locators.QUESTION_1, Locators.QUESTION_1_HEADER, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
         (Locators.QUESTION_2, Locators.QUESTION_2_HEADER, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
         (Locators.QUESTION_3, Locators.QUESTION_3_HEADER, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
         (Locators.QUESTION_4, Locators.QUESTION_4_HEADER, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
         (Locators.QUESTION_5, Locators.QUESTION_5_HEADER, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
         (Locators.QUESTION_6, Locators.QUESTION_6_HEADER, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
         (Locators.QUESTION_7, Locators.QUESTION_7_HEADER, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
         (Locators.QUESTION_8, Locators.QUESTION_8_HEADER, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")])

    def test_questions_important_waitfor_correct_header(self, driver, get_the_page, go_to_questions_important, the_question, question_header, expected_value):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((the_question))).click()
        actually_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((question_header))).text
        assert actually_value == expected_value, f"Заголовок вопроса должен быть '{expected_value}', но было '{actually_value}'"