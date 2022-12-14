import time
import unittest
from Pages.LoginPage import login
from Pages.MainPage import mainpage
from enviroment import setup_enviroment


class test_logout(unittest.TestCase):
    global login_page, main_page
    login_page = login
    main_page = mainpage

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

    def test_002_logout(self):
        main_page.click_hambuguer_menu(self)
        time.sleep(1)
        main_page.click_logout(self)
        current_url = self.driver.current_url
        self.assertEquals(current_url, "https://www.saucedemo.com/")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
