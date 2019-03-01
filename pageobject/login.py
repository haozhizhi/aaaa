from pageobject.base import BasePage
from selenium.webdriver.common.by import By
from framework.Logger import Logger
import  time
logger=Logger(logger="Homepage").getlog()
class  Homepage(BasePage):
    username_input=(By.NAME,"username")
    password_input=(By.NAME,"password")
    login_button=(By.TAG_NAME,"button")
    name=(By.CSS_SELECTOR,".vwmy>a")

    #发帖
    link_moren = (By.CSS_SELECTOR, ".bm_c .fl_tb tr:nth-child(1) td:nth-child(2)  h2 a")
    # link_moren=(By.CSS_SELECTOR,".fl_tb tr h2 a")#默认板块
    linkb = (By.CSS_SELECTOR, "#category_1 tr:nth-last-child(2) h2 a")#歌曲模块
    sendmessagge=(By.NAME,"subject")
    textare =(By.NAME,"message")
    sendbutton = (By.CSS_SELECTOR,".ptm  strong")

    #回帖
    homekey=(By.CSS_SELECTOR,".nvhm")

    zezo=(By.CSS_SELECTOR,".num a")

    replytext=(By.CSS_SELECTOR,"#fastpostmessage")
    replybutton=(By.ID,"fastpostsubmit")

    #删帖
    fangkuai=(By.CSS_SELECTOR,".o input")
    delmessage=(By.LINK_TEXT,"删除")
    delbutton=(By.CSS_SELECTOR,"#modsubmit  span")

   #管理中心
    link_manager=(By.LINK_TEXT,"管理中心")
    adminpassword=(By.NAME,"admin_password")
    adminbutton=(By.CSS_SELECTOR,".loginnofloat input")
    link_luntan=(By.LINK_TEXT,"论坛")

    addmodel=(By.CSS_SELECTOR,".lastboard>a")
    newmodelname=(By.NAME,"newforum[1][]")
    model_submit=(By.ID,"submit_editsubmit")
    managexit=(By.LINK_TEXT,"退出")
    exit=(By.LINK_TEXT,"退出")

    #搜索haotest的帖子
    searchhao=(By.CSS_SELECTOR,".scbar_txt_td  input")
    seaechbutton=(By.CSS_SELECTOR,".scbar_btn_td  button ")
    #断言是否相等
    #帖子详情里标题
    haotest_title=(By.ID,"thread_subject")
    detailhao = (By.CSS_SELECTOR, ".xs3 a")

    #投票
    sendtiebuttona=(By.CSS_SELECTOR,"#pgt img")#发帖
    sendtiebuttonb=(By.CSS_SELECTOR,".mbw  li:last-of-type")#发起投票
    friote=(By.ID,"subject")#第一个框
    secvote=(By.CSS_SELECTOR,".mbm  p:nth-child(1)  input")#第二个框
    thvote=(By.CSS_SELECTOR,".mbm p:nth-child(2)  input")#第三个框
    fovote=(By.CSS_SELECTOR,".mbm p:nth-child(3)  input")#第四个框
    fivote=(By.TAG_NAME,"body")
    votebutton=(By.CSS_SELECTOR,".mbm button")#提交投票

    option=(By.ID,"option_1")
    toupiaobutton=(By.CSS_SELECTOR,".pn span")

    toupianname=(By.CSS_SELECTOR,".pcht  tr:nth-child(1) .pvt label")
    precent=(By.CSS_SELECTOR,".pcht  tr:nth-child(2) td:last-of-type")
    toupianname2 = (By.CSS_SELECTOR, ".pcht  tr:nth-child(3)  .pvt label")
    precent2 = (By.CSS_SELECTOR, ".pcht  tr:nth-child(4)  td:last-of-type")
    toupianname3 = (By.CSS_SELECTOR, ".pcht  tr:nth-child(5)  .pvt label")
    precent3 = (By.CSS_SELECTOR, ".pcht  tr:nth-child(6)  td:last-of-type")

    topic=(By.CSS_SELECTOR,".ts span")
    def handlers(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])
    def goiframe(self,n):
        self.driver.switch_to.frame(n)
    def  login(self,username,password):
         self.sendkeys(username,*self.username_input)
         self.sendkeys(password,*self.password_input)
         self.click(*self.login_button)

         return self.find_element(*self.name).text
    def  sendt(self,sendmessage,textare):
        # self.forward()
        self.click(*self.link_moren)
        self.sendkeys(sendmessage,*self.sendmessagge)
        self.sendkeys(textare,*self.textare)
        self.click(*self.sendbutton)
    def replymessage(self,replytie):
        # self.back()
        # self.forward()
        self.click(*self.homekey)
        self.click(*self.link_moren)
        self.click(*self.zezo)
        self.sendkeys(replytie,*self.replytext)
        self.click(*self.replybutton)
    def deltie(self):
        self.click(*self.link_moren)
        self.click(*self.fangkuai)
        self.click(*self.delmessage)
        self.click(*self.delbutton)
    def managermodel(self,adminpwd,newname):
        self.click(*self.link_manager)
        self.handlers(1)
        self.sendkeys(adminpwd,*self.adminpassword)
        self.click(*self.adminbutton)
        self.click(*self.link_luntan)
        self.goiframe(0)
        self.click(*self.addmodel)

        self.clear(*self.newmodelname)
        # logger.info("清楚成功")
        self.sendkeys(newname,*self.newmodelname)
        time.sleep(5)
        self.click(*self.model_submit)
        self.switch_window()
        time.sleep(7)
        self.click(*self.managexit)#管理中心退出
        self.switch_window()
        self.click(*self.exit)#用户退出
    #新板块下发帖
    def newmodelsend(self,title,content):
        self.handlers(0)
        self.click(*self.linkb)
        self.sendkeys(title, *self.sendmessagge)
        self.sendkeys(content, *self.textare)
        self.click(*self.sendbutton)
    def newmodelreply(self,replycontent):
        self.click(*self.homekey)
        self.click(*self.linkb)
        self.handlers(0)
        self.click(*self.zezo)
        self.get_windows_img()
        self.sendkeys(replycontent, *self.replytext)
        self.click(*self.replybutton)
        self.click(*self.exit)

    def search(self,content):
        self.sendkeys(content,*self.searchhao)
        self.click(*self.seaechbutton)
        self.handlers(1)
        self.click(*self.detailhao)
        self.get_windows_img()
        self.handlers(2)
        return self.find_element(*self.haotest_title).text

    def vote(self,firstvote,secondvote,threevote,fourvote,fivevote):
        self.click(*self.link_moren)
        time.sleep(10)
        self.click(*self.sendtiebuttona)
        time.sleep(5)
        self.click(*self.sendtiebuttonb)
        time.sleep(5)
        self.sendkeys(firstvote,*self.friote)
        self.sendkeys(secondvote,*self.secvote)
        self.sendkeys(threevote,*self.thvote)
        self.sendkeys(fourvote,*self.fovote)
        self.goiframe(0)
        self.sendkeys(fivevote,*self.fivote)
        self.handlers(0)
        self.click(*self.votebutton)
        time.sleep(5)
        self.click(*self.option)
        self.click(*self.toupiaobutton)
        self.handlers(0)
        n=self.find_element(*self.toupianname)
        m=self.find_element(*self.precent)
        n2 = self.find_element(*self.toupianname2)
        m2 = self.find_element(*self.precent2)
        n3 = self.find_element(*self.toupianname3)
        m3= self.find_element(*self.precent3)
        them=self.find_element(*self.topic)

        logger.info("名称%s"%n.text)
        logger.info("比例%s"% m.text)
        logger.info("名称%s"%n2.text)
        logger.info("比例：%s"% m2.text)
        logger.info("名称%s"% n3.text)
        logger.info("比例：%s"% m3.text)
        logger.info("主题%s"%them.text)
        self.click(*self.exit)



