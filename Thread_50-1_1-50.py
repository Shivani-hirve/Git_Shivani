# Que 7.5 : Display 1 to 50 and 50 to 1 using multithread

import threading
from time import sleep

def Thread1(No):
    print("Thread1 = 1 to 50")
    while No <= 50:
        print(No)
        No = No + 1

def Thread2(No):
    print("Thread2 = 50 to 1")
    while No >= 1:
        print(No)
        No = No - 1

def main():
    Number1 = 1
    Number2 = 50
    t1 = threading.Thread(target= Thread1, args = (Number1, ))
    t2 = threading.Thread(target= Thread2, args = (Number2, ))

    t1.start()
    sleep(1)
    print('-'*10)
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()    