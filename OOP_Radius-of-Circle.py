# Find Radius and Area of circle
PI = 3.14
class Circle:

    def __init__(self, Radius):
        self.A = Radius

    def CalculateArea(self):
        return (PI * self.A ** 2)

    def CalculateCircumference(self):
        return (2 * PI * self.A)

    def Display(self):
        return (self.A)

obj = Circle(int(input("Enter Radius of circle: ")))

Ans1 = obj.CalculateArea()
print("Area of Circle is: ",Ans1)

Ans2 = obj.CalculateCircumference()
print("Area of Circumference is: ",Ans2)

Ans3 = obj.Display()
print("Display Radius, Area, circumference: ", Ans3, "," , Ans2, "," , Ans1)