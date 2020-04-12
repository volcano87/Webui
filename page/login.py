from web.page.base_page import BasePage


class Login(BasePage):
    def login(self):
        self.get_cookies()
        pass