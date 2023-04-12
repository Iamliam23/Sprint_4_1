from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait



class MainPageQaScooter():

    def __init__(self, driver):
        self.driver = driver
    def click_yandex_link(self):
        window_1 = self.driver.window_handles[0]
        yandex_but = self.driver.find_element(*Locators.YANDEX_BUTTON)
        yandex_but.click()
        window_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(window_2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Locators.YANDEX_LOGIN_BUTTON)))

    def check_element_1(self):
        question_1 = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((Locators.QUESTION_1)))
        question_1.click()

    def question_header_1(self):
        return self.driver.find_element(*Locators.QUESTION_1_HEADER)

    def check_element_2(self):
        question_2 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_2)))
        question_2.click()

    def question_header_2(self):
        return self.driver.find_element(*Locators.QUESTION_2_HEADER)

    def check_element_3(self):
        question_3 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_3)))
        question_3.click()

    def question_header_3(self):
        return self.driver.find_element(*Locators.QUESTION_3_HEADER)

    def check_element_4(self):
        question_4 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_4)))
        question_4.click()

    def question_header_4(self):
        return self.driver.find_element(*Locators.QUESTION_4_HEADER)

    def check_element_5(self):
        question_5 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_5)))
        question_5.click()

    def question_header_5(self):
        return self.driver.find_element(*Locators.QUESTION_5_HEADER)

    def check_element_6(self):
        question_6 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_6)))
        question_6.click()

    def question_header_6(self):
        return self.driver.find_element(*Locators.QUESTION_6_HEADER)

    def check_element_7(self):
        question_7 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_7)))
        question_7.click()

    def question_header_7(self):
        return self.driver.find_element(*Locators.QUESTION_7_HEADER)

    def check_element_8(self):
        question_8 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((Locators.QUESTION_8)))
        question_8.click()

    def question_header_8(self):
        return self.driver.find_element(*Locators.QUESTION_8_HEADER)


















