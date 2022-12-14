import time
import unittest
from Pages.LoginPage import login
from Pages.MainPage import mainpage
from Pages.CartPage import cartpage
from Pages.CheckoutInformationPage import checkout_information
from Pages.CheckoutOverviewPage import checkout_overview
from enviroment import setup_enviroment


class test_logout(unittest.TestCase):
    global login_page, main_page, cart_page, checkout_information_page, checkout_overview_page
    login_page = login
    main_page = mainpage
    cart_page = cartpage
    checkout_information_page = checkout_information
    checkout_overview_page = checkout_overview

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = setup_enviroment.initialize_browser(inst, nav="chrome")
        inst.driver.maximize_window()
        # go to the page_testcafe
        inst.driver.get(login_page.url)

    def test_001_login(self):
        login.write_name(self, "standard_user")
        login.write_password(self, "secret_sauce")
        login.click_login(self)
        current_url = self.driver.current_url
        self.assertEquals(current_url, "https://www.saucedemo.com/inventory.html")

    def test_002_add_item_1(self):
        main_page.add_item(self, 0)
        time.sleep(1)
        self.assertEquals(main_page.number_of_items_on_cart(self), str(1))
        main_page.add_item(self, 2)
        time.sleep(1)
        self.assertEquals(main_page.number_of_items_on_cart(self), str(2))
        main_page.add_item(self, 4)
        time.sleep(1)
        self.assertEquals(main_page.number_of_items_on_cart(self), str(3))

    def test_003_go_to_cart(self):
        main_page.go_to_cart(self)
        current_url = self.driver.current_url
        self.assertEquals(current_url, "https://www.saucedemo.com/cart.html")

    def test_004_remove_item(self):
        cart_page.remove_bolt_tshirt(self)
        self.assertEquals(cart_page.number_of_items_on_cart(self), str(2))

    def test_005_go_to_checkout(self):
        cart_page.click_checkout(self)

    def test_006_write_info(self):
        checkout_information_page.write_name(self, 'Juan')
        checkout_information_page.write_lastname(self, 'Amador')
        checkout_information_page.write_zipcode(self, "12345")
        checkout_information.click_continue(self)
        current_url = self.driver.current_url
        self.assertEquals(current_url, "https://www.saucedemo.com/checkout-step-two.html")

    def test_007_verify_price(self):
        prices = checkout_overview.return_all_prices(self)
        total_price = float(prices[0].text[1::]) + float(prices[1].text[1::])
        item_total = checkout_overview.return_item_total_price(self)
        self.assertEquals(total_price, float(item_total.text[13::]))

    def test_008_finish_buy(self):
        checkout_overview.finish_buy(self)
        current_url = self.driver.current_url
        self.assertEquals(current_url, "https://www.saucedemo.com/checkout-complete.html")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
