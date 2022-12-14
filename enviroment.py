from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class setup_enviroment():

    def initialize_browser(self, nav):
        if nav == "chrome":
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            return driver

        elif nav == "firefox":
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
            return driver
        elif nav == "edge":
            service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
            return driver
