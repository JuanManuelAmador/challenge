import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

name_input = 'first-name'  # By ID
lastname_input = 'last-name'  # By ID
zipcode_input = 'postal-code'  # By ID
cta_continue = 'continue'  # By ID


class checkout_information(object):
    url = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, driver):
        self.driver = driver

    def write_name(self, name):
        wait = WebDriverWait(self.driver, 10)
        name_field = wait.until(lambda d: d.find_element(By.ID, name_input))
        name_field.clear()
        name_field.send_keys(name)

    def write_lastname(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        lastname_field = wait.until(lambda d: d.find_element(By.ID, lastname_input))
        lastname_field.clear()
        lastname_field.send_keys(lastname)

    def write_zipcode(self, zipcode):
        wait = WebDriverWait(self.driver, 10)
        zipcode_field = wait.until(lambda d: d.find_element(By.ID, zipcode_input))
        zipcode_field.clear()
        zipcode_field.send_keys(zipcode)

    def click_continue(self):
        wait = WebDriverWait(self.driver, 10)
        continue_ = wait.until(lambda d: d.find_element(By.ID, cta_continue))
        continue_.click()
        time.sleep(1)
