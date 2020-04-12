from time import sleep

from web.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index(reuse=True)

    def test_add_memeber(self):
        # goto_add_member实例化
        add_member = self.index.goto_add_member()
        # 添加成员
        add_member.add_member()
        sleep(2)
        assert '张四' in add_member.get_first()
