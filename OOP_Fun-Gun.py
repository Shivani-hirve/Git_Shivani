class Demo:

    value = 1
    def __init__(self, no1, no2):
        self.n1 = no1
        self.n2 = no2

    def fun(self):
        print (no1,no2)

    def gun(self):
        print(no1,no2)

no1 = int(input("Enter no1: "))
no2 = int(input("Enter no2: "))

obj1 = Demo(no1, no2)
obj2 = Demo(no1, no2)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()