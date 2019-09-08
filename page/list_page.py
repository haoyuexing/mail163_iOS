from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ListPage(BaseAction):

    sixteenth_line = By.XPATH, '//XCUIElementTypeStaticText[@name="第 16 行"]'

    fourth_line = By.XPATH, '//XCUIElementTypeStaticText[@name="第 4 行"]'

    def swipe_list(self):
        # 1.
        # s = self.find_element(self.sixteenth_line)
        # f = self.find_element(self.fourth_line)
        # self.driver.drag_and_drop(s, f)

        # 2.
        self.driver.execute_script("mobile: swipe", {"direction": "up"})




