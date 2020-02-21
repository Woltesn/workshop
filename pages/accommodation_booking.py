from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


class AccommodationBooking(BasePage):

    def fill_in_all_fields_accommodation(self):
        self.browser.find_element(By.NAME, 'first_name').clear()
        self.browser.find_element(By.NAME, 'first_name').send_keys('Dmitriy_selenium_test')
        self.browser.find_element(By.NAME, 'last_name').clear()
        self.browser.find_element(By.NAME, 'last_name').send_keys('Peternko_selenium_test')
        self.browser.find_element(By.NAME, 'reason').send_keys('For test')
        self.browser.find_element(By.NAME, 'arrival').click()
        self.browser.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]/a').click()
        self.browser.find_element(By.NAME, 'departure').click()
        self.browser.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[7]/a').click()
        self.browser.find_element(By.NAME, 'additional_remarks').send_keys('test')
        self.browser.find_element(By.CLASS_NAME, 'icon-booking').click()

        time.sleep(5)
