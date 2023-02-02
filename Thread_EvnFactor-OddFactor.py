# Que 7.2 : create two threads to calculate of factors of given even and odd number.

from time import sleep
import threading

def evenfactor(No):
    sum = 0
    for i in range(1, No, 1):
        if No % i == 0:
            if i % 2 == 0:
                sum = sum + i
    print("Sum of Even Factors: " ,sum)
    sleep(0.5)
            

def oddfactor(No):
    sum = 0
    for i in range(1, No, 1):
        if No % i == 0:
            if i % 2 != 0:
                sum = sum + i
    print("Sum of Odd Factors: " ,sum)      
    sleep(0.5)

def main():
    Number = int(input("Enter the Number: "))

    t1 = threading.Thread(target= evenfactor, args = (Number, ))
    t2 = threading.Thread(target= oddfactor, args = (Number, ))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    print("exit from main")

if __name__ == "__main__":
    main()
