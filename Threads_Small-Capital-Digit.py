# Que 7.4: Dispaly Small, Capital and Digits from given string

import threading
import os

def small(No):
    l = 0
    for i in No:
        if i.islower():
            l = l+1
    print("Number of small characters: ", l)

def capital(No):
    u = 0
    for i in No:
        if i.isupper():
            u = u+1
    print("Number of Capital characters: ", u)

def digits(No):
    N = 0
    for i in No:
        if i.isdigit():
            N = N+1
    print("Number of Digits: ",N)

def main():
    s = input("Enter Strings: ")

    t1 = threading.Thread(target= small, args = (s, ))
    t2 = threading.Thread(target= capital, args = (s, ))
    t3 = threading.Thread(target= digits, args = (s, ))

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    print("Id of small: ", id(small))
    t2.join()
    print("Id of capital: ", id(capital))
    t3.join()
    print("Id of digits: ", id(digits))


if __name__ == "__main__":
    main()