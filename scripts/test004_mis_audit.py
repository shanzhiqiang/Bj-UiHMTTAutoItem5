from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mis)
        # 获取 统一入口类
        self.page_in = PageIn(driver)
        # 调用登录业务成功方法（需要在PageMisLogin新增）
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        self.audit = self.page_in.page_get_PageMisAudit()

    # 结束
    def teardown_class(self):
        sleep(5)
        # 关闭driver
        GetDriver.quit_driver()

    # 审核文章测试方法
    def test_article_audit(self, title=page.article_title, channel=page.article_channel):
        # 调用审核业务方法
        self.audit.page_mis_audit(title, channel)
        try:
            # 断言
            assert self.audit.page_assert_success(title="bj-test17-004", channel="数据库")
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.audit.base_get_img()
            # 抛异常
            raise
