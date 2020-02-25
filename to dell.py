#
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pickle

driver = webdriver.Chrome('/home/dmitriy123/PycharmProjects/workshop_preproject/chrome_driver/chromedriver')
driver.get("https://dev.humanitarianbooking.wfp.org/en/countries/it/locations/88/facilities/65/form/")

cookies = pickle.load(open("/home/dmitriy123/PycharmProjects/workshop_preproject/cookies1.pkl", "rb"))
for cookie in cookies:

    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)
driver.refresh()
print(driver.maximize_window())
print(driver.())
#
# driver.get("https://dev.humanitarianbooking.wfp.org/en/countries/it/locations/88/facilities/65/form/")
# driver.find_element(By.ID, 'id_date_requested').click()
# time.sleep(2)
#
# chose_date = driver.find_element(By.CSS_SELECTOR, '#id_date_requested_table > tbody > tr:nth-child(3) > td:nth-child(6) > div').click()
# time.sleep(1)
# driver.find_element(By.NAME, 'last_name').send_keys("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

