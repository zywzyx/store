'''
1.编写一个函数cacluate, 可以接收任意多个数,
返回的是一个元组.元组的第一个值为所有参数的平均值,
第二个值是大于平均值的所有数average
'''
number_tuple = ()
number_list = [2,2]
arge = []


def cacluate ():

    #print(sum)

    while True:
        num = input('请输入数字')
        if num == 'q':
            sum = 0
            for i in number_list:
                sum = int(sum) + int(i)
            average = sum / len(number_list)
            arge.insert(0,int(average))
            for x in number_list:
                if int(x) > average:
                    arge.insert(1, x)
                    number_tuple = arge
                    print("值:", number_tuple)
            break
        else:
            number_list.append(int(num))
            print(number_list)





    #print(average)
   # return int(average)




cacluate()