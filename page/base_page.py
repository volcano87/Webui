import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    _drive = ""
    base_url = ""

    # driver要指定类型
    def __init__(self, reuse=False):
        # 如果driver为空，就复用已有的浏览器
        if reuse:
            chrome_opts = webdriver.ChromeOptions()
            # 设置 chrome debugging代理
            # 终端输入chrome -remote-debugging-port=9222,开启chrome_debug模式
            chrome_opts.debugger_address = '127.0.0.1:9222'
            # 复用浏览器
            self._driver = webdriver.Chrome(options=chrome_opts)
            # self.driver.get('https://work.weixin.qq.com/')
        else:
            # new chrome
            self._driver = webdriver.Chrome()
        if self.base_url != "":
            self._driver.get(self.base_url)
        # 隐式等待，解决元素加载过慢的问题
        self._driver.implicitly_wait(3)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def get_cookies(self):
        cookies = self._driver.get_cookies()
        with open("cookies.txt") as f:
            json.dump(cookies, f)

    def add_cookies(self):
        self._driver.get("https://work.weixin.qq.com/")
        with open('cookies.txt') as f:
            cookies: list[dict] = json.load(f)
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def wait_for(self, fuc):
        WebDriverWait(self._driver, 10).until(fuc)
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(by, locator))

    def teardown(self):
        self._driver.quit()
