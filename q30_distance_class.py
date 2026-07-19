

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other):
        total_inches = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        new_feet = total_inches // 12
        new_inches = total_inches % 12
        return Distance(new_feet, new_inches)

    def compare(self, other):
        total_self = self.feet * 12 + self.inches
        total_other = other.feet * 12 + other.inches

        if total_self > total_other:
            return "Distance 1 is greater"
        elif total_self < total_other:
            return "Distance 2 is greater"
        else:
            return "Both distances are equal"

d1 = Distance(5, 8)
d2 = Distance(4, 10)

sum_distance = d1.add(d2)
print(f"Distance 1 = {d1.feet}' {d1.inches}\"")
print(f"Distance 2 = {d2.feet}' {d2.inches}\"")
print(f"Sum = {sum_distance.feet}' {sum_distance.inches}\"")
print(d1.compare(d2))
