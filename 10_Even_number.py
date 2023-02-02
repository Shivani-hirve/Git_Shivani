# Que 9: Display 10 even numbers

def main():
    no = int(input("Enter a number: "))
    i = 1

    while i <= no:
        if i % 2 == 0:
            print(i)
        i = i + 1

if __name__ == "__main__":
    main()