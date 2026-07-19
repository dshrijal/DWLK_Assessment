
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks   

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return (self.total() / (len(self.marks) * 100)) * 100

    def division(self):
        perc = self.percentage()
        if perc >= 60:
            return "First Division"
        elif perc >= 45:
            return "Second Division"
        elif perc >= 33:
            return "Third Division"
        else:
            return "Fail"

students = [
    Student("Aarav", 1, [85, 78, 90, 88, 76]),
    Student("Priya", 2, [65, 70, 55, 60, 58]),
    Student("Rohan", 3, [40, 35, 38, 42, 30]),
    Student("Sita", 4, [95, 92, 89, 97, 90]),
    Student("Karan", 5, [50, 48, 55, 52, 45]),
]

for s in students:
    print(f"{s.name} (Roll {s.roll_number}) -> Total: {s.total()}, "
          f"Percentage: {s.percentage():.2f}%, Division: {s.division()}")
