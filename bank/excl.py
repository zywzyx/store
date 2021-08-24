import xlrd
from DBUtils import create
from DBUtils import update

excl =xlrd.open_workbook(filename=r"F:\PythonCode\python\2020.xlsx",encoding_override=True)

for i in range(12):
    st = excl.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    a = "shop_"
    i = i+1
    name = a + str(i)
<<<<<<< HEAD
    sql2 = "create table if not exists " + name +" like shop"
    sql1 =sql2
=======
    sql1 = "create table if not exists " + name +" like shop"

>>>>>>> 7a9e5576dc0b91a6f5e758ee8608c580337afaf8
    print(sql1)
    create(sql1)
    #插入数局
    for row in range(1,rows):
        ex = st.row_values(row)
<<<<<<< HEAD
        sql3 ="insert into "+name+" values(%s,%s,%s,%s,%s)"
        sql = sql3
=======
        sql ="insert into "+name+" values(%s,%s,%s,%s,%s)"
>>>>>>> 7a9e5576dc0b91a6f5e758ee8608c580337afaf8
        data = ex
        update(sql,data)
        print(ex)

