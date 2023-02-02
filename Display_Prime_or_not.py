# Que 5: Display given number is prime or not.

def main():
    no = int(input("Enter a number: "))
    for i in range (2, no):
        if (no % i) == 0:
            i += 1
            print(no,"is not a prime number")
    else:
        print(no, "is Prime number")

if __name__ == "__main__":
    main()