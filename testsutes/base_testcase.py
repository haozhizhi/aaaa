import unittest
from framework.brower_engine import BrowserEngine
import time
class  BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.be=BrowserEngine()
        self.driver=self.be.open_browser()
        time.sleep(10)
    def tearDown(self):
        self.be.quit_browser()