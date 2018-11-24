from selenium.webdriver.common.by import By
from base.base import Base

loc_username = By.ID, "com.vcooline.aike:id/etxt_username"
loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
loc_login_btn = By.ID, "com.vcooline.aike:id/btn_login"

# Page页面思路：
#             1. 一个页面一个对象 (新建一个Class)
#             2. 对象页面内需要操作的步骤，每一个步骤单独封装一个方法

class PageLogin(Base):

    # 输入用户名
    def page_input_username(self, text):
        self.base_input(loc_username, text)

    # 输入密码
    def page_input_pwd(self, text):
        self.base_input(loc_pwd, text)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(loc_login_btn)
