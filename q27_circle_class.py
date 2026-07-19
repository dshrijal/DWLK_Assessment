
class Circle:
    PI = 3.14159  

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def circumference(self):
        return 2 * Circle.PI * self.radius

circle1 = Circle(5)
circle2 = Circle(10)

print(f"Circle 1 -> Area: {circle1.area():.2f}, Circumference: {circle1.circumference():.2f}")
print(f"Circle 2 -> Area: {circle2.area():.2f}, Circumference: {circle2.circumference():.2f}")
