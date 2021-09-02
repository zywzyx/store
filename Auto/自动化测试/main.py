import unittest
from HTMLTestRunner import HTMLTestRunner
import os
from sentEmail import send
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

# 让运行器运行用例
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是HRK的登陆测试报告！",
    description="包含成功和失败的报告",
    verbosity=1,
    stream = open(file="HKR登录测试.html", mode ="w+", encoding="utf-8")
)

runner.run(tests)

send()









