from appium import webdriver


def get_appiumdriver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Redmi',
        # 'app': '/home/osboxes/py_practice/test_practice_proj/apks/TapShop.apk',
        'app': 'I:\\TapShop.apk',
        'apkPackage': 'com.tapshop.app.mobile'
    }
    driver = webdriver.Remote('http://192.168.31.101:4723/wd/hub', desired_caps)
    return driver
