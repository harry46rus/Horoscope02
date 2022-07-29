class Point():
    """Learn classes"""

    # def __init__(self):
    #     self.__counter=0

    circle=2
    line=1
    def __init__(self,x=0,y=0):
        self.__counter = 0
        self.x=x
        self.y=y

    def gipo(self):
        """расчет гипотинузы"""
        self.z=((self.x)**2+(self.y)**2)**0.5
        return self.z

    # def __del__(self):
    #     print('object deleted')

    def __call__(self, step=2, *args, **kwargs):
        """счетчик"""
        print("__call__")
        self.__counter+=step
        return self.__counter




class Mass(Point):
    circle = 4

    def gipo(self):
        self.z = self.x+self.y
        return self.z


a=Point(2,3)

b=Point(5,3)
c=Mass(7,3)

print(getattr(a,'z',6))

a()
a()
a()
a()
a(10)
zzz=c()*c()*c()

zz=a(10)
print(zz,zzz)
print(c.x)
print(c.y)
print(c.gipo())
print(a.x)
a.y=5
print(a.y)
print(a.gipo())


# print(b.__dict__)
#
# print(a.gipo())
#
# print(b.gipo())
#
# print(Point.gipo.__doc__)
# print(Point.circle)



