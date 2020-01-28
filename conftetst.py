import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome(executable_path="./chrome_driver/chromedriver")
    yield
    print("\nquit browser..")
    driver.quit()