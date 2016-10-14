import time
from fixture.session import SessionHelper
from fixture.coupon import CouponHelper
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Application:

    def __init__(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'
        self.driver = webdriver.Firefox(capabilities=caps)
        #self.driver.implicitly_wait(30)
        self.base_url = "http://ec2-52-31-177-160.eu-west-1.compute.amazonaws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.coupon = CouponHelper(self)

    def destroy(self):
        time.sleep(1)
        self.driver.quit()
