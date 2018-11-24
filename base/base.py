from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver
        
    # 查找元素,封装
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).\
            until(lambda x: x.find_element(*loc))

    # 点击元素,封装
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法,封装
    def base_input(self, loc, text):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(text)
