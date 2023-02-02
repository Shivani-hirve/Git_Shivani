# Class : Number
# Instance Variable : value
# Instance Method : ChkPrime(), ChkPerfect(), SumFactors(), Factors()

class Number:
    def __init__(self, n):
        self.Value = n
        
    def Factors(self):
        No = 0
        print("Factors of Given Number is: ")
        for i in range (1, (int(self.Value/2)+1)):
            if(self.Value % i == 0):
                print(i, end=' ')
                                

    def SumFactors(self):
        Sum = 0
        for i in range (1, (int(self.Value/2)+1)):
            if(self.Value % i == 0):
                Sum = Sum + i
        print("Addition of Factors are: ",Sum)

    def ChkPerfect(self):
        Sum = 0
        i = 1
        while i<= int(self.Value/2):
            if(self.Value % i == 0):
                Sum = Sum + i
            i+=1
        if(Sum == self.Value):
            print("Entered Value is Perfect Number")
        else:
            print("Entered Value is not Perfect Number")

    def ChkPrime(self):
        for i in range(1, int(self.Value/2),1):
            if(self.Value % i == 0):
                print("Entered Value is Prime Number")
                break
            else:
                print("Entered Value is not Prime Number")

def main():
    m = int(input("Please enter number: "))
    obj = Number(m)
    obj.Factors()
    print()
    print('-'*50)
    obj.SumFactors()
    print('-'*50)
    obj.ChkPerfect()
    print('-'*50)
    obj.ChkPrime()
    
if __name__ == "__main__":
    main()