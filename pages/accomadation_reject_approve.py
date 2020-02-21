from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccommodationRejectAccept(BasePage):

    def accommodation_accept(self):
        self.browser.find_element(By.XPATH, '/html/body/main/section[2]/div[3]/div[1]/a/button/span').click()
        self.browser.find_element(By.XPATH, '/html/body/main/section[2]/table/tbody/tr[2]/td[6]/a/div').click()
        self.browser.find_element(By.XPATH, '//*[@id="accept_button"]/span').click()
        self.browser.find_element(By.ID, 'guest_type_select').click()
        self.browser.find_element(By.XPATH, '//*[@id="guest_type_select"]/option[2]').click()
        self.browser.find_element(By.ID, 'available_sections_select').click()
        self.browser.find_element(By.XPATH, '/html/body/main/section[2]/fieldset/div[2]/div/section[1]/table/tbody/tr[2]/td[2]/select/option[2]').click()
        self.browser.find_element(By.XPATH, '//*[@id="confirm_acceptance_button"]/span').click()
        time.sleep(3)
        self.browser.find_element(By.XPATH, '/html/body/main/section[2]/fieldset/div[2]/div/section[2]/table/tbody/tr[2]/td/button/span').click()
        # self.element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located())

        time.sleep(5)



