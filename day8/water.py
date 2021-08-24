class water:
    __height = ""
    __volume = ""
    __color = ""
    __material = ""
    __liquid = ""

    def setHeight(self,height):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setVolume(self,volume):
        self.__volume = volume
    def getVolume(self):
        return self.__volume
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setMaterial(self,material):
        self.__material=material
    def getMaterial(self):
        return self.__material
    def setLiquid(self,liquid):
        self.__liquid =liquid
    def getLiquid(self):
        return self.__liquid
    def run(self):
        print("高度",height,"CM,容积",volume,"ML,颜色为",color,"的",material,"水杯","，用于盛装",liquid)
data = water()
height = input("高度：")
data.setHeight(height)
volume = input("容积：")
data.setVolume(volume)
color = input("颜色：")
data.setColor(color)
material = input("材质：")
data.setMaterial(material)
liquid = input("液体")
data.setLiquid(liquid)
data.run()
