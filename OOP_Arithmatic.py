# Accept 2 numbers and perform Addition, Subtraction, Multiplication and Division of it.

class Arithmatic:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def Add (self):
        return self.No1+self.No2

    def Sub (self):
        return self.No1-self.No2

    def Mult (self):
        return self.No1*self.No2 

    def Divi (self):
        return self.No1/self.No2 

def Accept():
    value1 = float(input("Enter 1st Number: "))
    value2 = float(input("Enter 2nd Number: "))

    obj = Arithmatic(value1 ,value2)

    Ans = obj.Add()
    print("Addition is: ", Ans)

    Ans = obj.Sub()
    print("Subtration is: ", Ans)

    Ans = obj.Mult()
    print("Multiplication is: ",Ans)

    Ans = obj.Divi()
    print("Division is: ",Ans)

if __name__ == "__main__":
    Accept()