# Addition of Prime numbers from the list

list5 = []

def ChkNum():
    sum1=0
    for i in list5:
        check = 1
        for j in range (2, i):
            if i%j == 0:
                check = 0
                break
        if check == 1 and i != 1:
            sum1 = sum1 + i

    print("Output: ",sum1)

def ListPrime():
    size5 = int(input("How many Numbers you want to store in this List: "))
       
    for i in range (1, size5+1):
        i = int(input("Enter your Elements: "))
        list5.append(i)
    print("Input Elements: ",list5)

    ChkNum()
   
if __name__ == "__main__":
    ListPrime()    