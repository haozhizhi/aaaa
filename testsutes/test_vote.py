from framework.Logger import Logger
from testsutes.base_testcase import BaseTestCase
from pageobject.login import Homepage
import time

logger=Logger(logger="voteCase").getlog()
class voteCase(BaseTestCase):
    def  test_voteCase(self):
        homepage=Homepage(self.driver)
        name= homepage.login("admin", "sa")
        self.assertEqual(name,"admin",name)
        time.sleep(10)
        if "admin"  in name:
            homepage.vote("aa","bb","cc","dd","ee")



