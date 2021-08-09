import string,random,sys






#主页
def interface():
    print('*********************')
    print('*    中国工商银行\t\t*')
    print('*    账户管理系统\t\t*')
    print('*      v1.0\t\t\t*')
    print('*********************')
    print('*1.开户\t\t\t\t*')
    print('*2.存钱\t\t\t\t*')
    print('*3.取钱\t\t\t\t*')
    print('*4.转账\t\t\t\t*')
    print('*5.查询\t\t\t\t*')
    print('*6.bye!\t\t\t\t*')
    print('*********************\n')




brankNames = ['中国工商银行']
Code = ['456789']
brankUser = {'中国工商银行':[{"账户":"2222","姓名":"zyw","密码":"2222","存款":500},{"账户":"3333","姓名":"zyx","密码":"3333","存款":500}]}
userlist = {'2222':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'010'}],'3333':[{'国家':'中国','省份':'河北','城市':'唐山','街道':'中山路','门牌号':'011'}]}
money = 0


#随机生成账号
userCode = ''.join(random.sample(string.digits, 8))
#开户

def user():
     print('账号:',userCode)
     userName = input('请输入姓名:')
     userPwd = input('请输入密码:')
     brankname = '中国工商银行'
     Country = input('请输入国家:')
     Province = input('请输入省份:')
     City = input('请输入城市:')
     Street = input('请输入街道:')
     Table = input('请输入门牌号:')
     if userCode not in Code:
          Code.append(userCode)
          if userName not in brankUser:
              brankUser[brankname]=[{"账户":userCode,"姓名":userName,"密码":userPwd,"存款":0}]
              userlist[userCode]=[{'国家': Country, '省份':Province,'城市':City,'街道':Street,'门牌号':Table}]
              print('开户成功！\n',brankUser)
              print(userlist)

     elif  len(brankUser[brankname]) == 100:
          print("该银行用户已满")
     else:
          if brankname in brankNames:
             brankUser[brankname].append( {"账户": userCode, "姓名": userName, "密码": userPwd, "存款": 0} )
             print('开户成功！\n', brankUser)



#存款
def putMoney():
   code = input('请输入账户:')
   for i in range(0,len(brankUser['中国工商银行'])):
       if code == brankUser['中国工商银行'] [i] ['账户']:
          money = float(input('请输入金额:'))
          brankUser['中国工商银行'] [i] ["存款"] += money
          print('存款成功，总金额为:',brankUser['中国工商银行'] [i] ["存款"])
          return True
   else:
      print('不存在')






#取钱
def getMoney():
    code = input('请输入账户:')
    pwd  = input('请输入密码:')
    for i in range(0,len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'] [i] ['账户'] and pwd == brankUser['中国工商银行'] [i] ['密码']:
            money = float(input('请输入取款金额'))
            if money < brankUser['中国工商银行'] [i] ['存款']:
                brankUser['中国工商银行'][i]['存款'] -= money
                print('取款成功，总余额为:', brankUser['中国工商银行'][i]["存款"])
            else:
                print('余额不足！')
                return True
    else:
        print('账户或密码错误！')
        return False

#转钱
def transferMoney():
    code = input('请输入转出账户:')
    pwd = input('请输入密码:')
    for i in range(0, len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'][i]['账户'] and pwd == brankUser['中国工商银行'][i]['密码']:
            transferCode = input('请输入转入账户:')
            for j in range(0, len(brankUser['中国工商银行'])):
                if transferCode == brankUser['中国工商银行'][j]['账户']:
                    money = float(input('请输入转出金额:'))
                    if money < brankUser['中国工商银行'][j]['存款']:
                        brankUser['中国工商银行'][i]['存款'] -= money
                        brankUser['中国工商银行'][j]['存款'] += money
                        print('转账成功，总余额为:', brankUser['中国工商银行'][i]["存款"])

                    else:
                         print('余额不足')
                return True
    else:
        print('账户或密码错误！')



#查询

def selectUser():
    code = input('请输入账户:')
    pwd = input('请输入密码:')
    for i in range(0, len(brankUser['中国工商银行'])):
        if code == brankUser['中国工商银行'][i]['账户'] and pwd == brankUser['中国工商银行'][i]['密码']:
            print( brankUser['中国工商银行'][i])
            for j in range(0, len(userlist[code])):
                print(userlist[code][j])
            return True


    else:
        print('账户不存在！')


#退出
def exit():
    print('感谢您的使用，下次再见')
    sys.exit()









#选项
def index():
  while True:
     interface()
     choose = int(input('输入序号以选择使用的功能:'))

     if choose == 1:
       user()
     elif choose ==2:
         putMoney()
     elif choose ==3:
         getMoney()
     elif choose ==4:
         transferMoney()
     elif choose ==5:
         selectUser()
     elif choose ==6:
         exit()


index()