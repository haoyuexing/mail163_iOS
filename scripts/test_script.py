import time

import pytest

from base.base_driver import init_ios_driver
from base.base_page import Page


class TestScript:

    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = init_ios_driver()
        self.page = Page(self.driver)

        def teardown():
            time.sleep(2)
            self.driver.quit()

        request.addfinalizer(teardown)

    def test_swipe(self):
        self.page.home.click_list()
        self.page.list.swipe_list()

    def test_baidu(self):
        self.page.home.click_baidu()
        self.page.baidu.input_keyword("hello")
        self.page.baidu.click_search()
