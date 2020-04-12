from selenium.webdriver.common.by import By

from web.page.add_member import AddMember
from web.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.ID, 'menu_contacts').click()

        def wait(driver):
            ele_len = len(self.finds(By.ID, 'username'))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            return ele_len >= 1

        self.wait_for(wait)
        # 对AddMember进行实例化
        return AddMember(reuse=True)

    # 添加成员
    def add_member(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        # 对添加成员实例化
        return AddMember(reuse=True)
