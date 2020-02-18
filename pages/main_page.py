from allure_commons.types import AttachmentType

from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
import allure
import datetime

@allure.severity(allure.severity_level.NORMAL)
class MainPage(BasePage):

    @allure.severity(allure.severity_level.MINOR)
    def from_main_page_to_booking_list(self):
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="positional-buttons"]/a[1]/button').click()
        self.browser.find_element(By.XPATH, '//*[@id="country"]').click()
        self.browser.find_element(By.XPATH, '//*[@id="country"]').send_keys('Van')
        self.browser.find_element(By.ID, 'fly').click()
        time.sleep(2)
        self.enter_button = self.browser.find_element_by_xpath('//*[@id="map"]/div[4]/div[2]/div/div[3]/a')
        self.enter_button.click()
        time.sleep(2)
        self.browser.find_element(By.ID, 'fly').click()
        # click on "Midgar HUB TEST"
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="country-map"]/div[2]/a')
        # click on "WFP Driver" pop-up
        self.browser.find_element(By.CLASS_NAME, 'info').click()
        time.sleep(1)
        # Click on "Request your booking" button
        self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[5]/div/a/span').click()

    @allure.severity(allure.severity_level.NORMAL)
    def fill_in_all_fields_driver(self):
        print("OK")
        self.browser.find_element_by_name('first_name').clear()
        self.browser.find_element_by_name('first_name').send_keys("Dmirtiy_selen_test")
        self.browser.find_element_by_name('last_name').clear()
        self.browser.find_element_by_name('last_name').send_keys("Petrenko_selen_test")
        self.browser.find_element_by_name('email').clear()
        self.browser.find_element_by_name('email').send_keys("dmitr.petrenko@anvileight.com")
        self.browser.find_element_by_name('phone_number').clear()
        self.browser.find_element_by_name('phone_number').send_keys('+380509761444')
        self.browser.find_element_by_name('agency').clear()
        self.browser.find_element_by_name('agency').send_keys('WFP')
        self.browser.find_element_by_name('index_number').clear()
        self.browser.find_element_by_name('index_number').send_keys('12')
        self.browser.find_element_by_id('id_manager_email').send_keys('dmitriy.petrenko+manager@anvileight.com')
        self.browser.find_element_by_id('id_n_of_passengers').send_keys('1')
        self.browser.find_element_by_id('airport_type_button').click()
        time.sleep(1)
        now = datetime.datetime.now()
        print(type(now.day))
        if len(str(now.day)) == 1:
            correct_day = ('0' + str(now.day))
            date_now = (correct_day + "/" + str(now.month) + "/" + str(now.year))
        elif len(str(now.month)) == 1:
            correct_month = ('0' + str(now.month))
            date_now = (str(now.day) + "/" + correct_month + "/" + str(now.year))
        else:
            date_now = (str(now.day) + "/" + str(now.month) + "/" + str(now.year))
        print('OTTTT')
        self.browser.find_element_by_xpath('//*[@id="id_bookedroute_set-0-pickup_date"]').click()
        time.sleep(0.3)
        self.browser.find_element_by_class_name('picker__button--today').click()
        time.sleep(0.3)
        self.browser.find_element_by_xpath('//*[@id="id_bookedroute_set-0-pickup_time"]').click()
        time.sleep(0.3)
        print('OKKKKK')
        self.browser.find_element_by_xpath(
            '//*[@id="id_bookedroute_set-0-pickup_time_root"]/div/div/div/div/ul/li[7]').click()
        time.sleep(0.3)
        self.browser.find_element_by_name('bookedroute_set-0-pickup_town').clear()
        time.sleep(0.3)
        self.browser.find_element_by_name('bookedroute_set-0-pickup_town').send_keys('Pick-up_town_test')
        time.sleep(0.3)
        self.browser.find_element_by_name('bookedroute_set-0-pickup_location').send_keys('test_location')
        self.browser.find_element_by_name('bookedroute_set-0-dropoff_town').clear()
        time.sleep(0.3)
        self.browser.find_element_by_name('bookedroute_set-0-dropoff_town').send_keys('Drop-off_town_test')
        time.sleep(0.3)
        self.browser.find_element_by_name('bookedroute_set-0-dropoff_location').send_keys('Drop-off_location_test')
        time.sleep(0.3)
        self.browser.find_element_by_id('id_flight_arrival_departure_time').click()
        time.sleep(0.3)
        self.browser.find_element_by_xpath(
            '//*[@id="id_flight_arrival_departure_time_root"]/div/div/div/div/ul/li[48]').click()
        self.browser.find_element_by_id('id_flight_number').send_keys('12')
        time.sleep(0.3)
        self.browser.find_element_by_id('id_remarks').send_keys(300 * 'a')
        time.sleep(0.3)
        self.browser.find_element_by_class_name('icon-booking').click()
        not_found = True
        try:
            self.browser.find_elements_by_link_text(
                "Your request has been sent successfully. You will receive a copy of your request at 123")
        except:
            allure.attach(self.browser.get_screenshot_as_png(), name="testBookingScreen",
                          attachment_type=AttachmentType.PNG)
            not_found = False
        assert not_found

    def fill_in_all_fields_accommodation(self):
        self.browser.find_element(By.NAME, 'first_name').send_keys('Dmitriy_selenium_test')
        self.browser.find_element(By.NAME, 'last_name').send_keys('Peternko_selenium_test')