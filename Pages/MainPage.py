import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

title = '//*[@id="header_container"]/div[2]/span'
hamburguer_menu= 'react-burger-menu-btn' #By ID
all_items_opt='inventory_sidebar_link'#By ID
about_opt='about_sidebar_link' #By ID
logout_opt='logout_sidebar_link' #By ID
reset_app_state_opt='reset_sidebar_link'#By ID

add_to_cart_backpack='add-to-cart-sauce-labs-backpack' #By ID
add_to_cart_bike_light='add-to-cart-sauce-labs-bike-light' #By ID
add_to_cart_bolt_tshirt='add-to-cart-sauce-labs-bolt-t-shirt' #By ID
add_to_cart_fleece_jacket='add-to-cart-sauce-labs-fleece-jacket' #By ID
add_to_cart_fleece_onesie='add-to-cart-sauce-labs-onesie' #By ID
add_to_cart_red_tshirt='add-to-cart-test.allthethings()-t-shirt-(red)' #By ID
items=[add_to_cart_backpack,add_to_cart_bike_light,add_to_cart_bolt_tshirt,add_to_cart_fleece_onesie,add_to_cart_fleece_jacket,add_to_cart_red_tshirt]

cart_icon='shopping_cart_link' #ByCLASSNAME
cart_counter='shopping_cart_badge' #ByCLASSNAME

class mainpage(object):
    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self,driver):
        self.driver = driver

    def click_hambuguer_menu(self):
        wait = WebDriverWait(self.driver, 10)
        menu_cta= wait.until(lambda d: d.find_element(By.ID, hamburguer_menu))
        menu_cta.click()
        time.sleep(0.5)

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10)
        logout_cta= wait.until(lambda d: d.find_element(By.ID, logout_opt))
        logout_cta.click()
        time.sleep(0.5)

    def add_item(self,item):
        wait = WebDriverWait(self.driver, 10)
        add_cart_cta = wait.until(lambda d: d.find_element(By.ID, items[item]))
        add_cart_cta.click()
        time.sleep(0.5)

    def number_of_items_on_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart_count = wait.until(lambda d: d.find_element(By.CLASS_NAME, cart_counter)).text
        return cart_count

    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart_cta = wait.until(lambda d: d.find_element(By.CLASS_NAME, cart_icon))
        cart_cta.click()
        time.sleep(1)



