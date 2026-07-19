
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        
        total_inches = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        new_feet = total_inches // 12
        new_inches = total_inches % 12
        return Distance(new_feet, new_inches)

    def __str__(self):
        
        return f"{self.feet}' {self.inches}\""

d1 = Distance(5, 8)
d2 = Distance(4, 10)

d3 = d1 + d2  

print("Distance 1:", d1)
print("Distance 2:", d2)
print("Sum (using + operator):", d3)
