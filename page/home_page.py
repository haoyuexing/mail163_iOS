from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    baidu_button = By.XPATH, '//XCUIElementTypeStaticText[@name="百度"]'

    list_button = By.XPATH, '//XCUIElementTypeStaticText[@name="列表"]'

    alert_button = By.XPATH, '//XCUIElementTypeStaticText[@name="提示弹窗"]'

    drag_button = By.XPATH, '//XCUIElementTypeStaticText[@name="拖动"]'

    def click_baidu(self):
        self.click(self.baidu_button)

    def click_list(self):
        self.click(self.list_button)

    def click_alert(self):
        self.click(self.alert_button)

    def click_drag(self):
        self.click(self.drag_button)
