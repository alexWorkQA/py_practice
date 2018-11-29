import os

from appium import webdriver


class Application():

    def initialization(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Redmi',
            'app': self.PATH('../../apks/TapShop.apk'),


        }
        return webdriver.Remote('http://', desired_caps)

    def PATH(p):
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
