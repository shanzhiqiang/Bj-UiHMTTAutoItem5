from base.base import Base
import page


class PageAppLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.app_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断我的是否存在
    def page_if_element_exists(self):
        try:
            el = self.base_find(page.app_me, timeout=3)
            print("找到我的菜单了！它的位置位于：{}".format(el.location))
            return True
        except:
            print("没找到我的菜单")
            return False

    # 组合登录业务方法
    def page_app_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合登录业务方法
    def page_app_login_success(self, username="13812345678", pwd="246810"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
