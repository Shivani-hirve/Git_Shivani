# Que 7.1 : Create a two thread which display 10 even numbers and 10 Odd numbers
from time import sleep
import os
import threading

def Even(No):
    for i in range(1, No+1):
        if i % 2 == 0:
            print("Even Number: ", i)
            
def Odd(No):
    for i in range(1, No+1):
        if i % 2 != 0:
            print("Odd Numer: ", i)

def main():
    Number = 20

    t1 = threading.Thread(target= Even, args = (Number, ))
    t2 = threading.Thread(target= Odd, args = (Number, ))

    t1.start()
    sleep(1)
    t2.start()
   
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()