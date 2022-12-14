import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

continue_shopping_cta = 'continue-shopping'  # By ID
checkout_cta = 'checkout'  # By ID

remove_backpack = 'remove-sauce-labs-backpack'  # By ID
remove_bolt_tshirt = 'remove-sauce-labs-bolt-t-shirt'  # By ID
remove_onesie = 'remove-sauce-labs-onesie'  # By ID
cart_counter = 'shopping_cart_badge'  # by_classname


class cartpage(object):
    url = "https://www.saucedemo.com/cart.html"

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        checkout = wait.until(lambda d: d.find_element(By.ID, checkout_cta))
        checkout.click()
        time.sleep(1)

    def remove_bolt_tshirt(self):
        wait = WebDriverWait(self.driver, 10)
        remove_bolt_tshirt_cta = wait.until(lambda d: d.find_element(By.ID, remove_bolt_tshirt))
        remove_bolt_tshirt_cta.click()
        time.sleep(1)

    def number_of_items_on_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart_count = wait.until(lambda d: d.find_element(By.CLASS_NAME, cart_counter)).text
        return cart_count
