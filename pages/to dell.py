# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome(executable_path="/home/dmitriy123/PycharmProjects/workshop_preproject/chrome_driver/chromedriver")
# browser.get("https://www.google.com.ua/?hl=ru")
# time.sleep(10)


import pickle
import selenium.webdriver
import selenium.webdriver

driver = selenium.webdriver.Chrome(executable_path="/home/dmitriy123/PycharmProjects/workshop_preproject/chrome_driver/chromedriver")
driver.get("https://dev.humanitarianbooking.wfp.org/en/")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    dripages/to dell.py:17er.add_cookie(cookie)

    driver.find_element().click()