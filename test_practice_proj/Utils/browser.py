from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Browser(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def tap_button(self, selector):
        element = self.driver.get_element(selector)

        #something like logger
        element.click()

    def wait_elemnt(self, selector):
        self.wait.until(expected_conditions.presence_of_element_located(By.XPATH))

