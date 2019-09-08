from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text = By.ID, "com.netease.mail:id/editor_email"

    password_edit_text = By.ID, "com.netease.mail:id/editor_password"

    add_button = By.ID, "com.netease.mail:id/register_button_next"

    def input_username(self, text):
        self.input(self.username_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_add(self):
        self.click(self.add_button)

