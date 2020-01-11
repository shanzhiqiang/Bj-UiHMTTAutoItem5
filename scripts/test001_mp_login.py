
import pytest

from tools.read_yaml import read_yaml
# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()
import page

from page.page_in import PageIn

from tools.get_driver import GetDriver


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取PageMpLogin对象
        self.login = PageIn(self.driver).page_get_PageMpLogin()
        print("参数化读取数据为：", read_yaml("mp_login.yaml"))

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, phone, code, expect):
        # 调用登录业务方法
        self.login.page_mp_login(phone, code)
        try:
            # 断言
            assert expect == self.login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise
