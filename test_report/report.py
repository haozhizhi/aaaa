import unittest
from testsutes.test_login import testLoginCase
from testsutes.test_managercase import managerCase
from testsutes.test_search import searchCase
from testsutes.test_vote import voteCase

import HTMLTestRunner
import os
#获取当前路径testall1文件所在的路径
cur_path=os.path.dirname(os.path.realpath(__file__))
#将测试报告放在当前路径下的report中
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
#将abc_test ,sort_test加入到suite中

suite=unittest.TestSuite()#实列化suite
#suite.addTest(unittest.makeSuite(AbsTestCase))

suite.addTest(unittest.makeSuite(testLoginCase))
suite.addTest(unittest.makeSuite(managerCase))
suite.addTest(unittest.makeSuite(searchCase))
suite.addTest(unittest.makeSuite(voteCase))

if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试",description="用例执行情况")
    runner.run(suite)