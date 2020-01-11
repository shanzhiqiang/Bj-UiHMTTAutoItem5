from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    """
    存储 app应用专属方法
    """

    def base_app_right_to_left(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取区域位置
        location = el.location
        y = location.get("y")
        # 获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x,start_y,end_x,end_y
        start_x = width * 0.8
        start_y = y+height * 0.5
        end_x = width * 0.2
        end_y = y+height * 0.5
        # 组合find_text包含的元素定位信息
        #//android.widget.HorizontalScrollView表示父级频道区域框的属性
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]".format(find_text)
        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            # 首先查找一次当前页面是否存在，要找的元素
            try:
                el = self.base_find(loc, timeout=2)
                el.click()
                # 找到后就可以跳出循环额
                break

            except:
                # 没找到就继续找，滑动
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
                # self.driver.swipe(start_x=940, start_y=309, end_x=4, end_y=315, duration=2000)
            if page_source == self.driver.page_source:
                raise Exception
            else:
                # 更新page_source的值
                page_source = self.driver.page_source

    def base_app_down_to_up(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)

        # 获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x,start_y,end_x,end_y
        start_x = width * 0.5
        start_y = height * 0.85
        end_x = width * 0.5
        end_y = height * 0.15
        # 组合find_text包含的元素定位信息
        #//*[@bounds='[0,390][1080,1716]']表示父级频道区域框的属性
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(find_text)
        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            # 首先查找一次当前页面是否存在，要找的元素
            try:
                el = self.base_find(loc, timeout=2)
                print("找到的文章标题为：{}".format(el.text))
                el.click()
                # 找到后就可以跳出循环额
                break

            except:
                # 没找到就继续找，滑动
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

            if page_source == self.driver.page_source:
                raise Exception
            else:
                # 更新page_source的值
                page_source = self.driver.page_source
