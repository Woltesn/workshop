from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


class ClicnicBooking(BasePage):

    def fill_in_all_fields_clinic(self):
        self.browser.find_element(By.NAME, 'first_name').send_keys('Dmitriy_selen')
        self.browser.find_element(By.NAME, 'last_name').send_keys('Petrenko_selen')
        self.browser.find_element(By.NAME, 'email').clear()
        self.browser.find_element(By.NAME, 'email').send_keys('dmytro.petrenko@anvileight.com')
        self.browser.find_element(By.NAME, 'phone_number').send_keys('+380509761444')
        self.browser.find_element(By.NAME, 'agency').send_keys('anvil8 for test')
        self.browser.find_element(By.NAME, 'index_number').send_keys('12')
        self.browser.find_element(By.NAME, 'policy_number').send_keys('12')
        self.browser.find_element(By.NAME, 'contract').click()

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
        # self.browser.find_element(By.ID, 'id_date_requested').click()

        # chose_date = self.browser.find_element(By.CSS_SELECTOR, '#id_date_requested_table > tbody > tr:nth-child(3) > td:nth-child(6) > div').click()

        self.browser.find_element(By.ID, 'id_date_requested').send_keys("21/02/2020")
        time.sleep(1)
        self.browser.find_element(By.XPATH, '/html/body/main/section/div[2]/form/div[6]/div[2]/span/div/div/div/div/div/table/tbody/tr[4]/td[6]/div').click()
        time.sleep(1)
        self.browser.find_element(By.ID, 'id_time_of_visit').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="id_time_of_visit_root"]/div/div/div/div/ul/li[18]').click()
        time.sleep(1)
        self.browser.find_element(By.ID, 'id_reason_for_consultation').click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="id_reason_for_consultation"]/option[2]').click()
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, 'icon-booking').click()
        time.sleep(1)