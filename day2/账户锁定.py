start = 1
while start <= 3:
    print('第',start,'次登录')
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    if name == 'admin' and pwd =='root':
       print('登录成功')
       break
    else:
       print('登录失败')
    start = start + 1
while start == 4:
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    print('账户已锁定')
    break