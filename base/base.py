import allure
from selenium.webdriver.support.wait import WebDriverWait

# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()
class Base:
    # 初始化 driver
    def __init__(self, driver):
        log.info("正在初始化driver:{}".format(driver))
        self.driver = driver

    # 查找 元素  --> 给输入、点击、获取文本方法使用
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 定位一组元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 输入 方法
    def base_input(self, loc, value):
        # 调用查找元素
        el = self.base_find(loc)
        log.info("正在执行清空操作")
        # 清空操作
        el.clear()
        log.info("正在给 {} 元素 执行输入操作：{}".format(loc, value))
        # 输入操作
        el.send_keys(value)

    # 点击 方法
    def base_click(self, loc):
        log.info("正在对 {} 元素 执行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取 文本方法
    def base_get_text(self, loc):
        log.info("正在获取{}元素文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error("出现异常！正在截图操作")
        # 截图
        self.driver.get_screenshot_as_file("./images/err.png")
        # 调用将图片写入报告
        self.__base_write_img()

    # 将图片写入allure报告
    def __base_write_img(self):
        log.error("异常处理！正在截图写入报告")
        with open("./images/err.png","rb")as f:
            allure.attach("错误原因：",f.read(),allure.attach_type.PNG )
