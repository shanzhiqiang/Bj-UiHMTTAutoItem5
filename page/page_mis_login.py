from base.base import Base
import page


class PageMisLogin(Base):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        # 改变按钮为可点状态
        js = "document.getElementById('inp1').disabled=false"
        # 调用执行js语句方法
        self.driver.execute_script(js)
        # 点击登录按钮
        self.base_click(page.mis_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 登录组合业务方法
    def page_mis_login(self,username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 登录组合业务方法
    def page_mis_login_success(self,username="testid", pwd="testpwd123"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()