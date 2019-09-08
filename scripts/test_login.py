import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from base.base_page import Page


class TestLogin:

    devices = [
        {"udid": "192.168.56.101:5555", "port": "4723", "sys_port": "8200"},
        {"udid": "192.168.56.103:5555", "port": "4725", "sys_port": "8201"},
    ]

    @pytest.fixture(params=devices, autouse=True)
    def setup(self, request):
        self.driver = init_driver(request.param)
        self.page = Page(self.driver)

        def teardown():
            self.driver.quit()

        request.addfinalizer(teardown)

    def test_login(self):
        self.page.login.input_username("hitfeat@163.com")
        self.page.login.input_password("hitfeat123000")
        self.page.login.click_add()
        assert "已成功添加的邮箱" == self.page.res.get_title_text()

