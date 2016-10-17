import time

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        driver = self.app.driver
        self.open_login_page()
        driver.find_element_by_css_selector("div#main form.auth input[name='email']").clear()
        driver.find_element_by_css_selector("div#main form.auth input[name='email']").send_keys(email)
        driver.find_element_by_css_selector("div#main form.auth input[name='password']").clear()
        driver.find_element_by_css_selector("div#main form.auth input[name='password']").send_keys(password)
        driver.find_element_by_css_selector("div#main form.auth .btn.btn-primary").click()

    def ensure_login(self, email, password):
        driver = self.app.driver
        if not self.is_logged_in():
            self.login(email, password)

    def logout(self):
        driver = self.app.driver
        driver.get(self.app.base_url + "/open-eshop-2.0.1/oc-panel/auth/logout")
        #time.sleep(1)

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def open_login_page(self):
       driver = self.app.driver
       driver.get(self.app.base_url + "/open-eshop-2.0.1/oc-panel/auth/login")