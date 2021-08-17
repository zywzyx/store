def math(a,b):
    print(a)

    if a<b:
       return math(a+1,b)
    else:
        return -1

math(1,150)


sum = 0
def num(a,b):
    global sum
    if a<=b:
        sum = sum + a
        a = a+1
        return num(a,b)
    else:
        print(sum)


num(1,300)