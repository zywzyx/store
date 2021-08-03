i = 1
while i < 10:
      k = 1
      while k <= i:
          print('%d*%d=%2d   '% (i,k,i*k),end='')
          k += 1
      print()
      i += 1


n = 9
while n >0:
    m = 1
    while m <= n:
        print('%d*%d=%2d   '% (n,m,n*m),end='')
        m += 1
    print()
    n-=1