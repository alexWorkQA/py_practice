from selenium.webdriver.support.wait import WebDriverWait

from Helpers.driver_helper import get_appiumdriver


class Application:

    def __init__(self):
        self.driver = get_appiumdriver()

    def complete(self):
        self.driver.quit()
