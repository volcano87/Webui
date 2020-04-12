from selenium.webdriver.common.by import By

from web.page.base_page import BasePage


class AddMember(BasePage):
    # 在添加成员页面实现输入内容并保存
    def add_member(self):
        # 输入内容
        self.find(By.ID, 'username').send_keys('张四')
        self.find(By.ID, 'memberAdd_english_name').send_keys('zhangsan')
        self.find(By.ID, 'memberAdd_acctid').send_keys('ffsss')
        self.find(By.ID, 'memberAdd_phone').send_keys('11123454321')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        elems = self.finds(By.CSS_SELECTOR, '#member_list>tr:nth-child(1) >td:nth-child(2)')
        arrs = []
        for elem in elems:
            arrs.append(elem.get_attribute('title'))
        return arrs
