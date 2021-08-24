class Air:
    __company = "格力"
    __price = "5800"
    def setCompany(self,company):
        self.__company = company
    def getCompany(self):
        return self.__company
    def setPrice(self,prcie):
        self.__price =prcie
    def getPrice(self):
        return self.__price

    def start(self):
        print("空调开机了")
    def time(self,i):

        print("空调将在",i,"分钟后关机")

A = Air()

print(A.getCompany(),"空调，价格：",A.getPrice())
A.start()
time = int(input("时间"))
A.time(time)
