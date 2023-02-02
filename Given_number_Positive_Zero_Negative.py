# Que 6: Display given number is positive, negative or zero

def main():
    no = int(input("Enter any Number: "))
    if no > 0:
        print("Positive Number")
    
    elif no == 0:
        print("Zero")
    
    else: 
        print("Negative Number")        

if __name__ == "__main__":
    main()