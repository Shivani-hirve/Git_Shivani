# Display Factorials of given number

def main():
    no = int(input("Enter any Number: "))

    i = 1
    while no > 0:
        i = i * no
        no = no - 1
    print("Factorials: ", i)


if __name__ == "__main__":
    main()

no = int(input("Enter any Number: "))

for i in range (0, no):
    i = i * no
print(i)