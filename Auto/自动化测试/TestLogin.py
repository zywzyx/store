import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from Initpage import InitPage
from LoginPage import LoginPage
from selenium import webdriver
import time
import xlrd
import xlwt
from xlutils.copy import copy
# 用例 ： 整合页面的操作和调用页面的数据
# 打开想要更改的excel文件
# 打开想要更改的excel文件
old_excel = xlrd.open_workbook(filename=r"F:\PythonCode\python\Auto\自动化测试\test.xlsx",
                               encoding_override=True)
# 将操作文件对象拷贝，变成可写的workbook对象
st = old_excel.sheet_by_name('Sheet1')
new_excel = copy(old_excel)
ws = new_excel.get_sheet(0)
rows = st.nrows
@ddt

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 在每个用例执行前
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    def tearDown(self) -> None: # 在每个用例执行完后执行
        time.sleep(1)
        self.driver.quit()


    # 登陆成功用例
    @data(*InitPage.login_success_data)
    def testLoginSuccess(self,testdata):
        #1.提取用户名和密码和期望数据
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # 创建页面的对象，并把driver传给他
        login = LoginPage(self.driver)
        # 2.登陆
        login.login(username,password)

        # 3.提取成功的实际结果
        result = login.get_success_data()

        # 4.断言
        #self.assertEqual(expect,result)

        if result != expect:
            self.driver.save_screenshot("loginfail.jpg")
            for row in range(1, rows):
                name = st.cell_value(row, 0)
                pwd = st.cell_value(row, 1)
                ex = st.cell_value(row, 2)
                if name == username and pwd == password and ex == expect:
                    # 写入数据
                    ws.write(row, 3, '不通过')
                    # 另存为excel文件，并将文件命名
                    new_excel.save('TestCase.xlsx')
        else:
            for row in range(1, rows):
                name = st.cell_value(row, 0)
                pwd = st.cell_value(row, 1)
                ex = st.cell_value(row, 2)
                if name == username and pwd == password and ex == expect:

            # 写入数据
                    ws.write(row, 3, '通过')
            # 另存为excel文件，并将文件命名
                    new_excel.save('TestCase.xlsx')


    @data(*InitPage.login_pwd_error_data1)
    def testLoginError(self, testdata):
        # 1.提取用户名和密码和期望数据
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # 创建页面的对象，并把driver传给他
        login = LoginPage(self.driver)
        # 2.登陆
        login.login(username, password)

        # 3.提取成功的实际结果
        result = login.get_error_pwd_data()

        # 4.断言
       # self.assertEqual(expect, result)

        if result != expect:

            self.driver.save_screenshot('loginfail.jpg')
            for row in range(1, rows):
                name = st.cell_value(row, 0)
                pwd  = st.cell_value(row,1)
                ex   = st.cell_value(row,2)
                if name == username and pwd == password and ex == expect:
                    # 写入数据
                    ws.write(row, 3, '不通过')
                    # 另存为excel文件，并将文件命名
                    new_excel.save('TestCase.xlsx')
        else:
            for row in range(1, rows):
                name = st.cell_value(row, 0)
                pwd  = st.cell_value(row,1)
                ex   = st.cell_value(row,2)
                if name == username and pwd == password and ex ==expect :
                    # 写入数据
                    ws.write(row, 3, '通过')
                    # 另存为excel文件，并将文件命名
                    new_excel.save('TestCase.xlsx')
