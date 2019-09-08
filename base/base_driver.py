from appium import webdriver


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'huawei'
    # udid
    # desired_caps['udid'] = para["udid"]
    # app信息
    desired_caps['appPackage'] = 'com.netease.mail'
    desired_caps['appActivity'] = 'com.netease.mobimail.activity.InitAddAccountActivity'
    # # 不重置应用
    # desired_caps['noReset'] = True
    # toast
    # desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['systemPort'] = para['sys_port']
    # 解决中文问题
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://127.0.0.1:%s/wd/hub' % "4723", desired_caps)



def init_ios_driver():

    desired_caps = dict()
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '12.4'
    desired_caps['deviceName'] = 'iPhone 8'
    desired_caps['app'] = 'com.itfeat.testDemo'
    desired_caps['startIWDP'] = True
    desired_caps['clearSystemFiles'] = True
    desired_caps['automationName'] = "XCUITest"

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
