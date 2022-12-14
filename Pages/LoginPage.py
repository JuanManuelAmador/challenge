import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

username_input = 'user-name'  # By ID
password_input = 'password'  # By ID
login_button = 'login-button'  # By ID


class login(object):
    url = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def write_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        name_input = wait.until(lambda d: d.find_element(By.ID, password_input))
        name_input.clear()
        name_input.send_keys(password)
        time.sleep(1)

    def click_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_cta = wait.until(lambda d: d.find_element(By.ID, login_button))
        login_cta.click()
        time.sleep(2)

    def write_name(self, name):
        wait = WebDriverWait(self.driver, 10)
        name_input = wait.until(lambda d: d.find_element(By.ID, username_input))
        name_input.clear()
        name_input.send_keys(name)
        time.sleep(1)
