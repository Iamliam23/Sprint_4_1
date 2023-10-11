from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators



class CheckHeaderLinks():

    def __init__(self, driver):
        self.driver = driver

    def click_scooter_link(self):
        order_but_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((Locators.ORDER_BUTTON_1)))
        order_but_1.click()
        scooter_but = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((Locators.SCOOTER_BUTTON)))
        scooter_but.click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def click_yandex_link(self):
        window_1 = self.driver.window_handles[0]
        yandex_but = self.driver.find_element(*Locators.YANDEX_BUTTON)
        yandex_but.click()
        window_2 = self.driver.window_handles[1]
        self.driver.switch_to.window(window_2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Locators.YANDEX_LOGIN_BUTTON)))
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'


