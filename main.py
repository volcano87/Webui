from time import sleep

from selenium import webdriver
import json

from selenium.webdriver.common.by import By


class TestTest:
    def setup(self):
        chrome_opts = webdriver.ChromeOptions()
        # 设置 chrome debugging代理
        # 终端输入chrome -remote-debugging-port=9222,开启chrome_debug模式
        chrome_opts.debugger_address = '127.0.0.1:9222'
        # 复用浏览器
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(3)

    def test_test(self):
        # cookies = self.driver.get_cookies()
        # with open('cookies.txt', 'w') as f:
        #     json.dump(cookies, f)
        with open('cookies.txt', 'r') as f:
            cookies: list[dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def teardown(self):
        self.driver.quit()
