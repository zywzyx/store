'''
跨地区转账利率1%
'''
from DBUtils import update
from DBUtils import select
import string, random, sys

info = '''
    ------------个人信息----------------
    账号：%s,
    用户名：%s,
    取款密码：%s,
    ------------地址信息----------------
    国家：%s,
    省份：%s,
    街道：%s,
    门牌号：%s,
    余额：%s,
    开户行：%s
    账户类型：%s
    -----------------------------------
                '''


def page():
    print("*************************************")
    print("*           中国工商银行              *")
    print("*           账户管理系统              *")
    print("*              V1.0                 *")
    print("*************************************")
    print("*1、开户                             *")
    print("*2、存钱                             *")
    print("*3、取钱                             *")
    print("*4、转账                             *")
    print("*5、查询                             *")
    print("*6、Bye!                            *")
    print("*" * 37)


# 开户
def add_user():

    code = ''.join(random.sample(string.digits, 8))

    user = int(input("请选择您的账户类型(输入1为一类账户，输入2为二类账户)："))
    if user == 1 or user ==2:

        print("账号:", code)
        name = input("请输入您的姓名：")
        pwd = input("请输入账户密码：")
        country = input("请输入国家：")
        province = input("请输入省份：")
        street = input("请输入街道：")
        house = input("请输入门牌号：")
        money = input("请输入初始存入金额：")
        bank = "中国农业银行"
        sql = "select count(*) from ABC"
        data = select(sql, [])
        if data[0][0] >= 100:
            print("账户已满")
            return 3
        sql1 = "select * from ABC where code = %s"
        data1 = select(sql1, code)  # (("张三"),(“李四”))
        if len(data1) != 0:
            print("对不起，该用户已存在！请稍后重试！！！")
            return 2
        else:
            # print(code, name, pwd, country, province, street, house, money,bank)
            sql2 = "insert into abc values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2 = [code, name, pwd, country, province, street, house, money, bank, user]
            update(sql2, param2)
            sql3 = "select * from abc where code = %s"
            data2 = select(sql3, code)
            # print(data2[0][1])
            print("恭喜开户成功！")

            print(info % (
            data2[0][0], data2[0][1], data2[0][2], data2[0][3], data2[0][4], data2[0][5], data2[0][6], data2[0][7],
            data2[0][8],data2[0][9]))
            return 1
    else:
        print("请输入正确的账户类型！")


# 存钱
def save_money():
    code = input('请输入账号:')
    sql = "select * from abc where code = %s"
    data = select(sql, code)
    if len(data) == 1:
        money = float(input("请输入存款金额:"))
        money = money + float(data[0][7])
        print(money)
        sql1 = "update abc set money=%s where code=%s"
        parma = [money, code]
        update(sql1, parma)
        data1 = select(sql, code)
        print("存款成功！")
        print(info % (
        data1[0][0], data1[0][1], "*****", data1[0][3], data1[0][4], data1[0][5], data1[0][6], data1[0][7],
        data1[0][8],data1[0][9]))


# 取钱
def get_money():
    code = input('请输入账号:')
    sql = "select * from abc where code = %s"
    data = select(sql, code)
    if len(data) == 1:
        pwd = input('请输入密码:')
        if pwd == data[0][2]:
            money = float(input("请输入存款金额:"))
            money = float(data[0][7]) - money
            print(money)
            sql1 = "update abc set money=%s where code=%s"
            parma = [money, code]
            update(sql1, parma)
            data1 = select(sql, code)
            print("取款成功！")
            print(info % (
                data1[0][0], data1[0][1], "*****", data1[0][3], data1[0][4], data1[0][5], data1[0][6], data1[0][7],
                data1[0][8],data1[0][9]))
        else:
            print('密码错误')


# 转账
def tr_money():
    code = input('请输入账号:')
    sql = "select * from abc where code = %s"
    data = select(sql, code)
    if len(data) == 1:
        pwd = input('请输入密码:')
        if pwd == data[0][2]:
            recode = input('请输入转入账号:')
            sql1 = "select * from abc where code = %s"
            data1 = select(sql1, recode)
            sql4 = "select * from iabc where code = %s"
            data4 = select(sql4, recode)
            if len(data1) == 1:
                mon= float(input('请输入转出金额:'))
                money = float(data[0][7]) - mon
                trmoney = float(data1[0][7]) + mon
                print(money)
                #转出账户转出金钱
                sql2 = "update abc set money=%s where code= %s"
                parma2 = [money, code]
                update(sql2, parma2)
                data2 = select(sql, code)
                print("转账成功！")
                print(info % (
                    data2[0][0], data2[0][1], "*****", data2[0][3], data2[0][4], data2[0][5], data2[0][6], data2[0][7],
                    data2[0][8],data2[0][9]))
                #转入账户收到金钱
                sql3 = "update abc set money=%s where code= %s"
                parma3 = [trmoney, recode]
                update(sql3, parma3)

            elif len(data4) == 1:
                mon = float(input('请输入转出金额:'))
                money = float(data[0][7]) - mon
                trmoney = float(data4[0][7]) + mon
                print(money)
                # 转出账户转出金钱
                sql5 = "update abc set money=%s where code= %s"
                parma5 = [money, code]
                update(sql5, parma5)
                data5 = select(sql, code)
                print("转账成功！")
                print(info % (
                    data5[0][0], data5[0][1], "*****", data5[0][3], data5[0][4], data5[0][5], data5[0][6], data5[0][7],
                    data5[0][8],data5[0][9]))
                # 转入账户收到金钱
                sql6 = "update iabc set money=%s where code= %s"
                parma6 = [trmoney, recode]
                update(sql6, parma6)
            else:
                print('账户不存在')
        else:
            print('密码错误')


# 查询
def lookup_user():
    code = input('请输入账号:')
    sql = "select * from abc where code = %s"
    data = select(sql, code)
    if len(data) == 1:
        pwd = input('请输入密码')
        if pwd == data[0][2]:
            print(info % (
            data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8],
            data[0][9]))
            return 1
        else:
            print('密码错误')
            return 2

    else:
        print('账号不存在')
        return 3


#
def interface():
    while True:
        page()
        choose = int(input("请选择需要办理的业务:"))
        if choose == 1:
            add_user()
        elif choose == 2:
            save_money()
        elif choose == 3:
            get_money()
        elif choose == 4:
            tr_money()
        elif choose == 5:
            lookup_user()
        elif choose == 6:
            print("Bye!")
            sys.exit()
        elif choose ==7:
            from IABC import select_user
            select_user()
            break
        else:
            print("请正确输入要办理的业务！")

interface()
