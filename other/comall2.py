# coding=utf-8

import unittest
import urllib
from core import constants
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
from core import commonutils
import string
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains as act
from selenium.webdriver.common.keys import Keys
import config
import os
import time
# import requests
# import json
#
# from jsonschema import validate
#
# from selenium import webdriver
# from core import commonutils
# from core import constants
# from selenium.webdriver.firefox.options import Options
# from core.logger import Logger as api_log
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Comall(object):
    u"""
       （简写了很多selenium方法），重写了一些方法；增加了
        一些类方法，以后框架开发主要是扩展这个类。
    """

    def __init__(self, browser='ff', headless=False):


        """
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        if browser == "firefox" or browser == "ff":
            # 增加headless方式运行firefox，同phantomjs，无浏览器窗口运行
            # 需要firefox version > 55时才能使用
            if headless:
                options = Options()
                options.add_argument("-headless")
                driver = webdriver.Firefox(executable_path='geckodriver', firefox_options=options)
            else:
                driver = webdriver.Firefox()
        elif browser == "chrome":
            # 增加headless方式运行chrome，同phantomjs，无浏览器窗口运行
            # 需要在chrome version > 59时才能使用
            if headless:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)


    def get_element(self, by_type, by_value):
        """获取基本元素对象"""
        if by_type == "id":
            return self.driver.find_element_by_id(by_value)
        elif by_type == "name":
            return self.driver.find_element_by_name(by_value)
        elif by_type == "xpath":
            return self.driver.find_element_by_xpath(by_value)
        elif by_type == "link":
            return self.driver.find_element_by_link_text(by_value)
        elif by_type == "class":
            return self.driver.find_element_by_class_name(by_value)
        elif by_type == "tag":
            return self.driver.find_element_by_tag_name(by_value)
        elif by_type == "css":
            return self.driver.find_element_by_css_selector(by_value)
        # 使用文字链接查找和定位
        elif by_type == "partial_link":
            return self.driver.find_element_by_partial_link_text(by_value)
        else:
            return False

    def get_elements(self, by_type, by_value):
        """获取基本元素组对象"""
        if by_type == "id":
            return self.driver.find_elements_by_id(by_value)
        elif by_type == "name":
            return self.driver.find_elements_by_name(by_value)
        elif by_type == "xpath":
            return self.driver.find_elements_by_xpath(by_value)
        elif by_type == "link":
            return self.driver.find_elements_by_link_text(by_value)

        elif by_type == "class":
            return self.driver.find_elements_by_class_name(by_value)
        elif by_type == "tag":
            return self.driver.find_elements_by_tag_name(by_value)
        elif by_type == "css":
            return self.driver.find_elements_by_css_selector(by_value)
        else:
            return False

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()

    def F5(self):
        """
        Refresh the current page.

        Usage:
        driver.F5()
        """
        self.driver.refresh()

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secs)

    def is_element_exists(self, by_type, by_value):
        u"""判断控件元素是否存在，返回boolean值"""
        flag = False
        try:
            self.get_element(by_type, by_value)
            flag = True
        except NoSuchElementException, e:
            flag = False

        return flag

    def is_not_element_exists(self, by_type, by_value):
        u"""判断控件元素不存在，返回boolean值"""
        flag = False
        try:
            self.get_element(by_type, by_value)
            flag = False
        except NoSuchElementException, e:
            flag = True

        return flag

    def until(self, by_type, by_value):
        u"""等待一个元素被找到，超时抛出异常，超时时间在configBase中设置"""
        res = False
        for i in range(1, config.element_find_wait, 1):
            self.debug_info(constants.el_to_wait % (by_type, by_value, str(i)))
            if self.is_element_exists(by_type, by_value):
                res = True
                break
            else:
                res = False
            time.sleep(1)

        if not res:
            raise NameError(constants.el_not_find % (
                by_type, by_value, str(config.element_find_wait)))

    def until_display(self, by_type, by_value):
        u"""等待一个元素显示，超时抛出异常，超时时间在configBase中设置"""
        res = False
        for i in range(1, config.element_display_wait, 1):
            self.debug_info(constants.el_to_wait % (by_type, by_value, str(i)))

            if self.is_display(by_type, by_value):
                res = True
                break
            else:
                self.isAlertPresent()
                res = False

        if not res:
            raise NameError(constants.el_not_find % (
                by_type, by_value, str(config.element_find_wait)))

    def is_page_load_complete(self):
        u"""判断web页面是不是加载完毕"""
        js = "return document.readyState"
        result = self.driver.execute_script(js)
        if result == "complete":
            return True
        else:
            return False

    def until_page_load(self):
        u"""等待一个页面加载完成，超时抛出异常，超时时间在configBase中设置"""
        res = False
        for i in range(1, config.element_find_wait, 1):
            if self.is_page_load_complete():
                res = True
                break
            else:
                res = False
            time.sleep(1)

        if not res:
            raise NameError(constants.Page_not_load % (
                str(config.element_find_wait)))

    def getcwd(self):
        """获得当前执行文件的系统路径"""
        return os.getcwd()

    def open(self, url):
        self.driver.get(url)

    def get_text(self, by_type, by_value):
        """获得控件元素的文本信息"""
        self.until_display(by_type, by_value)
        return self.get_element(by_type, by_value).text

    def click(self, by_type, by_value):
        """点击操作
        Usage:
        driver.click("xpath",el.login_submit_btn)
        """
        self.until_display(by_type, by_value)
        if self.is_element_exists(by_type, by_value):
            self.get_element(by_type, by_value).click()

    def get_attribute(self, by_type, by_value, attrname):
        """获取属性值

        Usage:
        """
        self.until_display(by_type, by_value)
        if self.is_element_exists(by_type, by_value):
            res = self.get_element(by_type, by_value).get_attribute(attrname)
            return res

    def send_keys(self, by_type, by_value, text):
        """文本输入操作

        Usage:
        driver.send_keys("xpath",el.login_submit_btn,"测试数据")
        """
        self.until_display(by_type, by_value)
        if self.is_element_exists(by_type, by_value):
            el = self.get_element(by_type, by_value)
            el.clear()
            el.send_keys(text)

    def switch_to_frame(self, n=0):
        """选择iframe"""
        n = int(n)
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[n])

    def switch_to_frame_by_xpath(self, xpath_el):
        """选择iframe"""
        self.driver.switch_to.frame(self.driver.find_elements_by_xpath(xpath_el)[0])

    def frame_list(self):
        return self.driver.find_elements_by_tag_name("iframe")

    def switch_to_frame_out(self):
        """退出iframe，回到上层"""
        self.driver._switch_to.default_content()

    def goto_newwindow(self):
        """跳转新的页面"""
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    def switch_next_window(self):
        """选择新打开的浏览器窗口，主要针对链接_blank打开的新窗口选择"""
        current_window = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != current_window:
                self.driver._switch_to.window(handle)

    def accept_alert(self):
        """处理弹出的alert框"""
        alert = self.driver._switch_to.alert
        print alert.text
        self.debug_info(alert.text)
        alert.accept()

    def dismiss_alert(self):
        """处理弹出的alert框"""
        alert = self.driver._switch_to.alert
        print alert.text
        self.debug_info(alert.text)
        alert.dismiss()

    def isAlertPresent(self):
        '''
        如果alert存在，则选择确定。
        :return:
        '''

        try:
            alert = self.driver._switch_to.alert
            alert.accept()
        except NoAlertPresentException, e:
            pass

    def file_upload_windows(self, file_path, driver_type):
        """windows文件上传，使用autoit生成的exe操作windows窗口"""
        command = config.base_dir + "tools\\" + "fileupload.exe " \
                  + driver_type + " " \
                  + file_path
        self.debug_info(command)
        try:
            os.system(command)
        except NoSuchElementException, e:
            print e.message

    def click_body(self):
        """点击空白，用于很多关闭临时悬浮窗口"""
        self.get_element("xpath", "/html/body").click()

    def move_to_element(self, by_type, by_value):
        """鼠标移动到指定元素"""
        el = self.get_element(by_type, by_value)
        self.until_display(by_type, by_value)
        act(self.driver).move_to_element(el).perform()

    def attr_check(self, by_type, by_value, attr_name, attr_value):
        """检查元素属性值是否符合期望，返回boolean值
        """
        self.until_display(by_type, by_value)
        attr = self.attr_get(by_type, by_value, attr_name)
        if attr == attr_value:
            return True
        else:
            return False

    def attr_get(self, by_type, by_value, attr_name):
        """获得element的属性值
        Usage:
        获得指定element的class值：dr.attr_get("xpath", el.index_login_user_edit, "class")
        """
        self.until_display(by_type, by_value)
        return self.get_element(by_type, by_value).get_attribute(attr_name)

    def is_display(self, by_type, by_value):
        """判断element是否显示，返回boolean值"""
        if self.is_element_exists(by_type, by_value):
            return self.get_element(by_type, by_value).is_displayed()

    def action_click(self, by_type, by_value):
        """激活使用鼠标事件"""
        if self.is_element_exists(by_type, by_value):
            a = self.get_element(by_type, by_value)
            act(self.driver).click(a).perform()

    def js_window_max(self):
        """chrome窗口最大化，调用js操作，解决在某些系统上无法最大化的问题"""
        js = "windowWidth = window.screen.availWidth;windowHeight = window.screen.availHeight;window.moveTo(0,0);window.resizeTo(windowWidth,windowHeight);"
        self.driver.execute_script(js)

    def debug_info(self, text):
        """调试信息是否打印，在config文件设置"""
        if config.debug:
            print text

    def win_key(self, by_type, by_value, key_name):
        u"""常用键盘操作
        目前支持：TAB\SPACE\ENTER\DELETE\SHIFT\ALT\CONTROL\ESC
        """
        if key_name == "TAB":
            win_key = Keys.TAB
        elif key_name == "PACE":
            win_key = Keys.SPACE
        elif key_name == "ENTER":
            win_key = Keys.ENTER
        elif key_name == "DELETE":
            win_key = Keys.DELETE
        elif key_name == "SHIFT":
            win_key = Keys.SHIFT
        elif key_name == "ALT":
            win_key = Keys.ALT
        elif key_name == "CONTROL":
            win_key = Keys.CONTROL
        elif key_name == "ESC":
            win_key = Keys.ESCAPE
        elif key_name == "cancel":
            win_key = Keys.CANCEL
        else:
            return False

        if self.is_element_exists(by_type, by_value):
            return self.get_element(by_type, by_value).send_keys(win_key)

    def scroll(self, scroll_type, scroll_value):
        u"""浏览器滚动条操作,从初始点移动到scroll_value像素
        Params：
            scroll_type:    top/left 向下滚动/向右滚动
            scroll_value:   滚动条操作变更的值，单位像素
        Usage:
            dr.scroll("window", "top", "300")   # 浏览器主窗口纵向滚动条，向下滚动300像素
        """
        scroll_value = int(scroll_value)
        if scroll_type == "top":
            self.js("window.scrollTo(0," + scroll_value + ")")
            return True
        elif scroll_type == "left":
            self.js("window.scrollTo(" + scroll_value + ",0)")
            return True
        return False

    def screen_shot(self, name_screen_shot):

        path = PATH(config.img_shot_dir)
        if not os.path.isdir(PATH(path)):
            os.makedirs(path)
        return self.driver.save_screenshot(path + '\\' + name_screen_shot + '.png')

    def assert_equal(self, unittest, first, second, msg, name_screen_shot):
        """
        :param first: 第一个比较字符串
        :param second: 第二个比较字符串
        :param msg: 断言信息
        :param name_ScreenShot:截图名称
        :return:
        """
        try:
            unittest.assertEqual(first, second, msg)
        # except Exception:
        # pass
        finally:
            self.screen_shot(name_screen_shot)
            time.sleep(5)
            pass