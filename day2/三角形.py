a=int (input("请输入A值："))
b=int (input("请输入B值："))
c=int (input("请输入C值："))

if a==b==c:
    print('等边三角形')
elif a==b or a==c or b==c:
    print('等腰三角形')
elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print('直角三角形')
elif a+b>c:
    print('普通三角形')
else:
    print('不构成三角形')
