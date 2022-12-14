import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

cta_cancel = 'cancel'  # By ID
cta_finish = 'finish'  # By ID
prices = 'inventory_item_price'  # classname
item_total = 'summary_subtotal_label'  # classname


class checkout_overview(object):
    url = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, driver):
        self.driver = driver

    def finish_buy(self):
        wait = WebDriverWait(self.driver, 10)
        finish = wait.until(lambda d: d.find_element(By.ID, cta_finish))
        finish.click()
        time.sleep(1)

    def cancel_buy(self):
        wait = WebDriverWait(self.driver, 10)
        cancel = wait.until(lambda d: d.find_element(By.ID, cta_cancel))
        cancel.click()
        time.sleep(1)

    def return_all_prices(self):
        wait = WebDriverWait(self.driver, 10)
        prices_list = wait.until(lambda d: d.find_elements(By.CLASS_NAME, prices))
        return prices_list

    def return_item_total_price(self):
        wait = WebDriverWait(self.driver, 10)
        item_total_price = wait.until(lambda d: d.find_element(By.CLASS_NAME, item_total))
        return item_total_price
