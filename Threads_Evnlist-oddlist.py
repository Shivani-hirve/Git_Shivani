# Que 7.3 : Addition of Even List and Addition of Odd list.
import threading
import os
from time import sleep

def evenlist(No):
    s = 0
    for i in No:
        if i % 2 == 0:
            s = s + i 
    print("Sum of Even Numbers: " ,s)
    sleep(0.5)

def oddlist(No):
    sum = 0
    for i in No:
        if i % 2 != 0:
            sum = sum + i
    print("Sum of Odd Numbers: " ,sum)
    sleep(0.5)

def main(): #10, 15, 20, 25, 30, 89, 13, 50
    l1= []
    print("Enter the Numbers: ")
    for i in range(1, 6, 1):
        i = int(input())
        l1.append(i)
    print("Given List: ", l1)

    t1 = threading.Thread(target= evenlist, args = (l1, ))
    t2 = threading.Thread(target= oddlist, args = (l1, ))

    t1.start()
    t2.start()


    t1.join()
    t2.join()


if __name__ == "__main__":
    main()