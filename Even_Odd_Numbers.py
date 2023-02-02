# Que 2: Display Given number is Even or Odd

def ChkNum():
    no = int(input("Enter any Number: "))
    if no % 2 == 0:
        print("Entered Number is Even")
    else:
        print("Entered Number is Odd")


if __name__ == "__main__":
    ChkNum()