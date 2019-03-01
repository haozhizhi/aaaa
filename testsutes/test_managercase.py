from framework.Logger import Logger
from testsutes.base_testcase import BaseTestCase
from pageobject.login import Homepage
import time
logger=Logger(logger="testmanagercase").getlog()

class managerCase(BaseTestCase):

    def test_manage(self):
        homepage=Homepage(self.driver)
        name=homepage.login("admin","sa")

        if "admin" in name:
            # homepage.deltie()
            time.sleep(10)
            homepage.managermodel("sa","ddd")
            # homepage.quit_browser()

            namenew=homepage.login("fwz","15935622817")

            if "fwz" in namenew:
                self.driver.switch_to.window(self.driver.current_window_handle)
                time.sleep(5)
                homepage.newmodelsend('小半小半','空空留遗憾多孤单心伤')
                time.sleep(5)
                homepage.newmodelreply("好好听好好听好好听好好听好好")
                time.sleep(5)







