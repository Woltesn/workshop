from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
import pickle


class MainPage(BasePage):
    def go_to_login_page(self):


        time.sleep(10)
        user_name = self.browser.find_element(By.ID, "id_username")
        user_name.send_keys("dmitriy.petrenko@wfp.org")
        login_button = self.browser.find_element(By.ID, "continue-button")
        login_button.click()
        time.sleep(10)

