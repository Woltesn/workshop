from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class ClicnicBooking(BasePage):

    def fill_in_all_fields_clinic(self):
        self.browser.find_element(By.NAME, 'first_name').send_keys('Dmitriy_selen')
        self.browser.find_element(By.NAME, 'last_name').send_keys('Petrenko_selen')
        self.browser.find_element(By.NAME, 'email').send_keys('dmytro.petrenko@anvileight.com')
        self.browser.find_element(By.NAME, 'phone_number').send_keys('+380509761444')
        self.browser.find_element(By.NAME, 'agency').send_keys('anvil8 for test')
        self.browser.find_element(By.NAME, 'index_number').send_keys('12')
        self.browser.find_element(By.NAME, 'policy_number').send_keys('12')
        self.browser.find_element(By.NAME, 'contract').click()
        time.sleep(0.5)
        self.browser.find_element(By.NAME, 'patient_name').send_keys('Dmitriy_selen_patient')
        time.sleep(0.5)
        self.browser.find_element(By.ID, 'id_date_of_birth').click()
        time.sleep(0.5)
        self.browser.find_element(By.CLASS_NAME, 'picker__button--clear').click()
        time.sleep(0.5)
        self.browser.find_element(By.ID, 'id_date_of_birth').click()
        time.sleep(0.5)
        self.browser.find_element(By.CLASS_NAME, 'picker__button--today').click()
        time.sleep(0.5)
        self.browser.find_element(By.ID, 'id_date_requested').click()
        time.sleep(0.5)
        chose_date = self.browser.find_element(By.CSS_SELECTOR, '#id_date_requested_table > tbody > tr:nth-child(3) > td:nth-child(6) > div').click()
        time.sleep(3)
        self.browser.find_element(By.NAME, 'last_name').send_keys("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        time.sleep(10)
        # time1 = self.browser.find_element(By.ID, 'id_time_of_visit').click()
        # time1 = self.browser.find_element(By.CSS_SELECTOR, "#id_time_of_visit_root > div > div > div > div > ul > li:nth-child(9)").click()


        # self.browser.find_element(By.ID, 'id_time_of_visit').click()
        # time.sleep(5)
        # self.browser.find_element(By.CSS_SELECTOR, '#id_time_of_visit_root > div > div > div > div > ul > li.picker__list-item.picker__list-item--highlighted.picker__list-item--viewset').click()
        # time.sleep(0.5)
        # self.browser.find_element(By.ID, 'id_reason_for_consultation').click()
        # time.sleep(5)
        # self.browser.find_element(By.LINK_TEXT, 'consultation').click()





