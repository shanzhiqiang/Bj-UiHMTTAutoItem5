import pytest

import page
from page.page_in import PageIn

from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mp)
        # 获取统一入口类
        self.page = PageIn(driver)
        # 调用登录业务成功方法
        self.page.page_get_PageMpLogin().page_mp_login_success()
        # 获取PageMpArticle对象
        self.article = self.page.page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试发布文章业务方法
    @pytest.mark.parametrize("title,content,expect", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect):
        # 调用发布文章业务方法
        self.article.page_publish_article(title, content)
        try:
            # 断言
            assert expect == self.article.page_get_commit_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise
