import xlrd

data = xlrd.open_workbook(filename=r"F:\PythonCode\python\Auto\自动化测试\test.xlsx",encoding_override=True)

st = data.sheet_by_name('Sheet1')
loginSucces_data = []
loginError_data = []
rows = st.nrows




class InitPage:
    for row in range(1, rows):

        name = st.cell_value(row, 0)
        pwd = st.cell_value(row, 1)
        ex = st.cell_value(row, 2)

        if row <= 2:

            true = {"username": name, "password": pwd, "expect": ex}
            loginSucces_data.append(true)
            print(loginSucces_data)
            login_success_data = loginSucces_data
        else:
            faile = {"username": name, "password": pwd, "expect": ex}
            loginError_data.append(faile)
            print(loginError_data)
    #id=msg_uname
            login_pwd_error_data1 =loginError_data
  #



