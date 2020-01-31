import pytest
from selenium import webdriver
import pickle

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('/home/dmitriy123/PycharmProjects/workshop_preproject/chrome_driver/chromedriver')
    yield browser
    print("\nquit browser..")
    browser.quit()