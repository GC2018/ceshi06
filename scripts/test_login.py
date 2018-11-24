import os, sys
sys.path.append(os.getcwd())
from base.get_driver import get_driver
from page.page_login import PageLogin

class TestLogin():

    # 实例化PageLogin
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self, username="15700002222", pwd="123456"):
        self.login.page_input_username(username)
        self.login.page_input_pwd(pwd)
        self.login.page_click_login_btn()
