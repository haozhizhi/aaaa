from framework.Logger import Logger
from testsutes.base_testcase import BaseTestCase
from pageobject.login import Homepage
import  unittest
logger=Logger(logger="testLoginCase").getlog()

class  testLoginCase(BaseTestCase):
    def test_LoginCase(self):
        self.home_page = Homepage(self.driver)
        name=self.home_page.login("admin","sa")

        self.assertEqual(name, "admin", msg=name)
        if 'admin'in name:
            self.home_page.sendt("haotest", "haotest")

            self.home_page.replymessage("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
            self.home_page.quit_browser()
if __name__=="__main__":
    unittest.main(verbosity=2)