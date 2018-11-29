import os
from time import sleep

import pytest
import unittest
from appium import webdriver


class simple_android_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Redmi',
            'app': '/home/osboxes/py_practice/test_practice_proj/apks/TapShop.apk',
            'apkPackage': 'com.tapshop.app.mobile'
        }
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_launch_app_test(self):
        assert False

    def PATH(p):
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), p))
