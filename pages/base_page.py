import pickle
import time

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):

        self.browser.get(self.url)
        cookies = pickle.load(open("/home/dmitriy123/PycharmProjects/workshop_preproject/cookies1.pkl", "rb"))
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        print(1)
        # time.sleep(40)
        # pickle.dump(self.browser.get_cookies(), open("cookies1.pkl", "wb"))
