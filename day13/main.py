from HTMLTestRunner import HTMLTestRunner # 专门测试用例，和生成报告
import unittest
import sentemail
# 1.将所有用例全部加载出来

tests = unittest.defaultTestLoader.discover(r"F:\PythonCode\python\day13",pattern="*test.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算器测试报告",
    description="这是计算器的加法测试报告",
    verbosity=1,
    stream = open(file="计算器报告.html",mode='w+',encoding='utf-8')
)


# 3.让运行器运行用例，并生成测试报告
runner.run(tests)
sentemail.send()

# 4.邮件发送，将计算器报告当成附件，邮件发送指向我
