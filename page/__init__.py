from selenium.webdriver.common.by import By

from tools.read_yaml import read_yaml

"""以下为黑马头条项目url"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

"""以下为文章配置数据"""
article_title = read_yaml("mp_article.yaml")[0][0]
article_channel = "数据库"

"""以下为自媒体配置数据"""
# 手机号
mp_phone = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 验证码
mp_code = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录
# mp_login = By.CSS_SELECTOR, ".el-button--primary"
mp_login = By.XPATH, "//*[text()='登录']/.."
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
# 点击内容管理
mp_content_manage = By.XPATH, "//div[@class='menu-wrapper']//*[text()='内容管理']"
# 点击发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 输入内容之前要切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道
mp_select_database = By.XPATH, "//*[text()='{}']".format(article_channel)
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"

"""以下为后台管理页面配置数据"""
# 用户名
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"
# 信息管理
mis_info_manage = By.XPATH, "//*[@class='menu']//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[@class='menu']//*[text()= '内容审核']"
# 标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询
mis_search = By.CSS_SELECTOR, ".find"
# 通过
mis_pass_btn = By.XPATH, "//*[text()='通过']/.."
# 确认通过
mis_confirm_pass = By.CSS_SELECTOR, ".el-button--primary"
# 文章id
mis_article_id = By.CSS_SELECTOR, ".cell>span"