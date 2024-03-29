import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pickle

@pytest.fixture(scope="function")
def browser():
    # capabilities = {
    #     "browserName": "chrome",
    #     "version": "79",
    #     "enableVNC": True,
    #     "enableVideo": False
    # }
    #
    # browser = webdriver.Remote(
    #     command_executor="http://127.0.0.1:4444/wd/hub",
    #     desired_capabilities=capabilities)

    print("\nstart browser for test..")
    browser = webdriver.Chrome('/home/dmitriy123/PycharmProjects/workshop_preproject/chrome_driver/chromedriver')
    browser.implicitly_wait(10)
    browser.wait = WebDriverWait(5, browser)
    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()




# class BaseSelenoidWebdriver(object):
#     def __init__(self):
#         self.capabilities = {
#             "browserName": "chrome",
#             "version": "80",
#             "enableVNC": True,
#             "enableVideo": False
#         }
#
#     def __enter__(self):
#         self.driver = webdriver.Remote(
#             command_executor="http://127.0.0.1:4444/wd/hub",
#             desired_capabilities=self.capabilities)
#         return self.driver
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.driver.close()
#
#
# if __name__ == '__main__':
#     with BaseSelenoidWebdriver() as webdriver:
#         webdriver.get('https://www.google.com.ua/?hl=ru')