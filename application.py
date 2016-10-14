from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from coupon import Coupon

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

    def login(self, email, password):
        driver = self.driver
        self.open_login_page()
        driver.find_element_by_css_selector("div#main form.auth input[name='email']").clear()
        driver.find_element_by_css_selector("div#main form.auth input[name='email']").send_keys(email)
        driver.find_element_by_css_selector("div#main form.auth input[name='password']").clear()
        driver.find_element_by_css_selector("div#main form.auth input[name='password']").send_keys(password)
        driver.find_element_by_css_selector("div#main form.auth .btn.btn-primary").click()

    def add_new_coupon(self, coupon):
        driver = self.driver
        # добавили ожидание 3 сек
        time.sleep(3)
        self.open_create_new_coupon_page()
        driver.find_element_by_css_selector("input#name").clear()
        driver.find_element_by_css_selector("input#name").send_keys(coupon.coupon_name)
        driver.find_element_by_css_selector("input[name='valid_date']").clear()
        driver.find_element_by_css_selector("input[name='valid_date']").send_keys(coupon.date)
        driver.find_element_by_css_selector("input#number_coupons").clear()
        driver.find_element_by_css_selector("input#number_coupons").send_keys(coupon.number_of_coupons)
        driver.find_element_by_css_selector(".btn.btn-primary[name='submit']").click()

    def find_and_delete_coupon(self, coupon_name):
        driver = self.driver
        self.open_coupons_page()
        driver.find_element_by_css_selector("div#content input.form-control[name='name']").clear()
        driver.find_element_by_css_selector("div#content input.form-control[name='name']").send_keys(coupon_name)
        driver.find_element_by_css_selector("div#content button.btn[type='submit']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-trash").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button.confirm").click()

    def open_login_page(self):
       driver = self.driver
       driver.get(self.base_url + "/open-eshop-2.0.1/oc-panel/auth/login")

    def open_create_new_coupon_page(self):
        driver = self.driver
        driver.get(self.base_url + "/open-eshop-2.0.1/oc-panel/Coupon/create/")

    def open_coupons_page(self):
        driver = self.driver
        driver.get(self.base_url + "/open-eshop-2.0.1/oc-panel/Coupon")

    def logout(self):
        driver = self.driver
        driver.get(self.base_url + "/open-eshop-2.0.1/oc-panel/auth/logout")

    def destroy(self):
        time.sleep(3)
        self.driver.quit()
