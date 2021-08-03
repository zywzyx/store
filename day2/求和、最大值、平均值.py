num = []
start = 1
while start <= 10:
    print("请输入您的第",start,"课成绩：")
    score =int (input())
    num.append(score)

    score = int(score)

    if score >= 90 and score <= 100:
        print("优秀！Excellent!")
    elif score >= 80 and score < 90:
        print("良好！good！")
    elif score >= 70 and score < 80:
        print("一般般！just so so！")
    elif score >= 60 and score < 70:
        print("小伙子，你很危险！")
    elif score >= 0 and score < 60:
        print("恭喜，您的试卷已经在路上了！")
    else:
        print("对不起，您的输入非法，请重新输入！")

    start = start + 1
    print(num)

    while start >= 11:
        print('总成绩为:',sum(num))
        print('最大值为:',max(num))
        print('最小值为:',min(num))
        print('平均值为:',sum(num)/10)
        break



