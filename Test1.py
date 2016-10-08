from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe'

driver = webdriver.Firefox(capabilities=caps)
time.sleep(2)
driver.get('http://google.com')