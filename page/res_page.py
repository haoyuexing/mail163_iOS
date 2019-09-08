from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ResPage(BaseAction):

    title_text_view = By.ID, "com.netease.mail:id/title"

    def get_title_text(self):
        return self.find_element(self.title_text_view).text
