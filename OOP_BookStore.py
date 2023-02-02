# Class: BookStore
# Instance Variable: Name, Author
# Class Variable: NoBooks

class BookStore:
    NoBooks = 1
    def __iniit__(self):
        
        self.Name = ""
        self.Author = ""

    def Display(self):
        self.Name = input("Name of Book: ")
        self.Author = input("Name of Author: ")

    def Increament(self):
        print("No of Books: ")
        for i in range(2):
            self.NoBooks = self.NoBooks + 1
        print(self.NoBooks)


def main():
    obj1 = BookStore()
    obj1.Display()
    obj1.Increament()

    obj2 = BookStore()
    obj2.Display()
    obj2.Increament()

main()