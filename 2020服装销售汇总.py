import xlrd

data = xlrd.open_workbook(filename=r"F:\PythonCode\python任务\2020.xlsx",encoding_override=True)
# cl = []
cl = {
    }
month_num=0
for i in range(12):
    st = data.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for row in range(1,rows):
        for col in range(cols):
            name = st.cell_value(row,1)
            price = st.cell_value(row,2)
            num = st.cell_value(row,4)
            if name not in cl:
                cl[name]={
                    "单价":price ,
                    "销售量":num
                }
            elif name in cl:
                cl[name]={
                    "单价": price,
                    "销售量":cl[name]["销售量"]+num
                }
print(cl)
money = 0
number = 0
for x in cl:
    money = cl[x]["单价"]*cl[x]["销售量"]+money
    number =cl[x]["销售量"]+number

print("全年销售量:",number,"件")
print('年销售额:','%.1f' % money,"元")
li = []
for y in cl:
    nm = cl[y]["销售量"] / number * 100
    li.append(y)
    print(y,'%.2f' %nm,"%")