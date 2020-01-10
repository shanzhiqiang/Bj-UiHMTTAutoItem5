from time import sleep

import page
from base.base import Base

# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(Base):

    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.mp_phone, phone)

    # 输入 验证码
    def page_input_verify_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击 登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login)

    # 获取 昵称
    def page_get_nickname(self):
        # 一定要返回
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 （测试脚本业务层调用）
    def page_mp_login(self, phone, code):
        log.info("正在调用自媒体登录业务方法，用户名：{} 密码：{}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

    # 组合业务方法 （测试脚本业务层调用）
    def page_mp_login_success(self, phone="13812345678", code="246810"):
        log.info("正在调用自媒体登录成功业务方法，用户名：{} 密码：{}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()