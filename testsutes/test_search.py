from framework.Logger import Logger
from testsutes.base_testcase import BaseTestCase
from pageobject.login import Homepage
import time
from ddt import ddt,data,unpack
import  unittest
logger=Logger(logger="testLoginCase").getlog()
@ddt

class searchCase(BaseTestCase):

    @unpack
    def test_SearchCase(self):
        homepage=Homepage(self.driver)
        name=homepage.login("admin",'sa')
        if "admin" in name:
            time.sleep(5)
            title=homepage.search("haotest")
            self.assertEqual(title,"haotest", msg=title)

if __name__=="__main__":
    unittest.main(verbosity=2)