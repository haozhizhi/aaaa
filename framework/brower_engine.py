import os.path
from  configparser import ConfigParser
from selenium import webdriver
from  framework.Logger import Logger

logger=Logger(logger="BrowserEngine").getlog()
class  BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir +"/tools/IEDriverServer.exe"
    firefox_driver_path=dir+"/tools/geckodriver.exe"

    def open_browser(self):
        config=ConfigParser()
        #读取config。ini的路径
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path,encoding="utf-8")

        browser=config.get("browserType","browserName")
        logger.info("选择浏览器%s"%browser)
        url=config.get("testServer","URL")
        logger.info("测试链接是%s"%url)
        #实例化driver
        if  browser=="Firefox":
            self.driver=webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("开始火狐浏览器")
        elif browser=="Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始chrome浏览器")
        else:
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("开始IE浏览器")
        self.driver.get(url)

        logger.info("打开链接%s"%url)
        self.driver.maximize_window()
        logger.info("最大窗口")
        self.driver.implicitly_wait(10)
        logger.info("等 10s")
        return  self.driver
    def quit_browser(self):
        logger.info("离开浏览器")
        self.driver.quit()

