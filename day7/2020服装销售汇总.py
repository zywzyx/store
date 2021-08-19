import xlrd

data = xlrd.open_workbook(filename=r"F:\PythonCode\python任务\2020.xlsx",encoding_override=True)
# cl = []
cl = {
    }
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

            break
print(cl)
money = 0
number = 0
for x in cl:
    money = cl[x]["单价"]*cl[x]["销售量"]+money
    number =cl[x]["销售量"]+number

print("全年销售量:",number,"件")
print('年销售额:','%.1f' % money,"元")

for y in cl:
    nm = cl[y]["销售量"] / number * 100
    nn = cl[y]["销售量"] * cl[y]["单价"] / money * 100
    print(y,"销售量", '%.2f' % nn, "%","销售额",'%.2f' %nm,"%")



min = max = cl["羽绒服"]["销售量"]


for i in cl:
    if max<cl[i]["销售量"]:
        max = cl[i]["销售量"]
        v = i
    if min >cl[i]["销售量"]:
        min =cl[i]["销售量"]
        m=i

print("最畅销的衣服:",v,max,"件")
print("销售最低的衣服:",m,min,"件")

