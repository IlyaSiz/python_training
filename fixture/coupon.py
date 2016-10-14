import time

class CouponHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, coupon):
        driver = self.app.driver
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


    def find_and_delete(self, coupon_name):
        driver = self.app.driver
        self.open_coupons_page()
        driver.find_element_by_css_selector("div#content input.form-control[name='name']").clear()
        driver.find_element_by_css_selector("div#content input.form-control[name='name']").send_keys(coupon_name)
        driver.find_element_by_css_selector("div#content button.btn[type='submit']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-trash").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button.confirm").click()

    def open_create_new_coupon_page(self):
        driver = self.app.driver
        driver.get(self.app.base_url + "/open-eshop-2.0.1/oc-panel/Coupon/create/")

    def open_coupons_page(self):
        driver = self.app.driver
        driver.get(self.app.base_url + "/open-eshop-2.0.1/oc-panel/Coupon")