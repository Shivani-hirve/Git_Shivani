# Class : BankAccount
# Instance Variables : Name & Amount
# Class Variables : ROI 
# Instance Method: Display(), Deposite(), Withdraw(), CalculateIntrest()
# Class Method : DisplayInformation

class BankAccount:
    ROI = 10.5

    def __init__(self, nam, amt):
        self.Name = nam
        self.Amount = amt

    def Display(self):
        print("Name of Holder = ",self.Name)
        print("Initial Amount = ",self.Amount)

    def Deposite(self):
        value = int(input("Enter the Amount for Deposite : "))
        self.Amount = self.Amount + value
        print("Amount After Deposite: ",self.Amount)
        

    def Withdraw(self):
        value = int(input("Enter the Amount for withdrawal : "))
        self.Amount = self.Amount - value
        print("Amount After Withdraw: ",self.Amount)
        
  
    def CalculateIntrest(self):
        Tenor = int(input("Enter How many Years: "))
        Intrest = ((self.Amount * self.ROI * Tenor)/100)
        print("Your Rate of Intrest is: ", Intrest)

def main():
    n = input("Enter name: ")
    a = int(input("Enter amount: "))
    obj = BankAccount(n,a)
    obj.Display()
    obj.Deposite()
    obj.Withdraw()
    obj.CalculateIntrest()
    
if __name__ == "__main__":
    main()