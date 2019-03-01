#_*_coding=utf-8 _*_
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as  EC
from  framework.Logger import Logger
import time
import os.path

logger=Logger(logger="base").getlog()

class BasePage(object):
    #初始化driver
    def __init__(self,driver):
        self.driver=driver
    #返回
    def back(self):
        self.driver.back()
        logger.info("返回当前页面")
    #前进
    def forward(self):
        self.driver.forward()
        logger.info("前进")
    #打开网页链接
    def open_url(self, url):
        self.driver.get(url)
        logger.info("open%s"%url)
    #离开浏览器
    def quit_browser(self):
        self.driver.quit()
        logger.info("quit browse")
    #获取当前窗口
    def switch_window(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    #获取当前打开的窗口
    def handlers(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])
    #进入iframe
    def goiframe(self,n):
        self.driver.switch_to.frame(n)
    #窗口最大
    def max_window(self):
        self.driver.maximize_window()
    #f5刷新
    def  F5(self):
        self.driver.refresh()
    #等待时间隐士等待
    def  wait(self,waittime):
        self.driver.implicitly_wait(waittime)
    #获得控件元素的文本信息
    def get_text(self,*loc):
        return  self.find_element(loc).text
    #获取属性值，type为css，id，。。。。
    def get_attribute(self,*loc,type):
        return self.find_element(loc).get_attribute(type)
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭离开浏览器")
        except Exception as e:
            logger.error("%s失败离开浏览器"%e)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))

            logger.info("%s找到页面元素%s"%(self,loc))
            return self.driver.find_element(*loc)
        except Exception as  e:
            logger.error("%s页面未找到%s元素"%(self,loc))
            #截屏
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("有截屏并且保存的路径是/screenshots/")
        except  Exception as  e:
            self.get_windows_img()
            logger.error("%s截屏失败"%e)
    def  sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except  Exception  as e:
            logger.info("失败输入内容%s"%e)
            self.get_windows_img()
    def clear(self,*loc):
        el=self.find_element(*loc)

        try:
            el.clear()
            logger.info("键入前清除文本框的内容")
        except Exception  as e:
            logger.error("%s清楚文本框内容失败"%e)
            self.get_windows_img()
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("被点击%s"%el)
        except Exception  as e:
            logger.error("没被点击%s"%el)