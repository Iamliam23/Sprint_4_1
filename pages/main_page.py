from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
import time



class MainPageQaScooter():

    def __init__(self, driver):
        self.driver = driver

    def check_element_1(self):
        question_1 = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((Locators.QUESTION_1)))
        question_1.click()
        qu_header_1 = self.driver.find_element(*Locators.QUESTION_1_HEADER)
        actually_value = qu_header_1.text
        expected_value = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 1 должен быть '{expected_value}', но было '{qu_header_1}'"

    def check_element_2(self):
        question_2 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_2)))
        question_2.click()
        qu_header_2 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_2_HEADER)))
        actually_value = qu_header_2.text
        expected_value = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 2 должен быть '{expected_value}', но было '{qu_header_2}'"

    def check_element_3(self):
        question_3 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_3)))
        question_3.click()
        qu_header_3 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_3_HEADER)))
        actually_value = qu_header_3.text
        expected_value = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 3 должен быть '{expected_value}', но было '{qu_header_3}'"

    def check_element_4(self):
        question_4 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_4)))
        question_4.click()
        qu_header_4 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_4_HEADER)))
        actually_value = qu_header_4.text
        expected_value = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 4 должен быть '{expected_value}', но было '{qu_header_4}'"

    def check_element_5(self):
        question_5 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_5)))
        question_5.click()
        qu_header_5 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_5_HEADER)))
        actually_value = qu_header_5.text
        expected_value = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 5 должен быть '{expected_value}', но было '{qu_header_5}'"

    def check_element_6(self):
        question_6 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_6)))
        question_6.click()
        qu_header_6 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_6_HEADER)))
        actually_value = qu_header_6.text
        expected_value = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 6 должен быть '{expected_value}', но было '{qu_header_6}'"

    def check_element_7(self):
        question_7 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_7)))
        question_7.click()
        qu_header_7 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_7_HEADER)))
        actually_value = qu_header_7.text
        expected_value = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 7 должен быть '{expected_value}', но было '{qu_header_7}'"

    def check_element_8(self):
        question_8 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_8)))
        question_8.click()
        qu_header_8 = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((Locators.QUESTION_8_HEADER)))
        actually_value = qu_header_8.text
        expected_value = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        WebDriverWait(self.driver, 10)
        assert actually_value == expected_value, f"Заголовок вопроса 8 должен быть '{expected_value}', но было '{qu_header_8}'"


















