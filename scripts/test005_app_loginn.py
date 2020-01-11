from page.page_in import PageIn
from tools.get_driver import GetDriver
import pytest

from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 通过统一入口类获取PageAppLogin对象
        self.app_login = PageIn(driver).page_get_PageAppLogin()

    # 关闭
    def teardown_class(self):
        GetDriver.quit_app_driver()

    # 调用测试方法
    @pytest.mark.parametrize("username,pwd", read_yaml("app_login.yaml"))
    def test_app_login(self, username, pwd):
        # 调用app登录业务方法
        self.app_login.page_app_login(username, pwd)

        try:
            # 断言是否登录成功
            assert self.app_login.page_if_element_exists()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.app_login.base_get_img()
            # 抛异常
            raise