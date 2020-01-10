from time import sleep

from base.base import Base
import page


class PageMpArticle(Base):
    # 点击 内容管理
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入 文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入 文章内容
    def page_input_article_content(self, content):
        # 切换 iframe
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        # 输入内容
        self.base_input(page.mp_content, content)
        # 切换到默认目录
        self.driver.switch_to.default_content()

    # 选择 封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # 选择 频道
    def page_click_channel(self):
        # 点击 选择频道
        self.base_click(page.mp_select)
        sleep(1)
        # 选择 具体频道
        self.base_click(page.mp_select_database)

    # 点击 发表
    def page_click_commit(self):
        self.base_click(page.mp_commit)

    # 获取发布 结果提示信息
    def page_get_commit_result(self):
        return self.base_get_text(page.mp_commit_result)

    # 组合发布业务方法
    def page_publish_article(self, title,content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_article_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_commit()