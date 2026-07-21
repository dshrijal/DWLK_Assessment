math = float(input("Enter the marks in Mathematics: "))
physics = float(input("Enter the marks in Physics: "))
chemistry = float(input("Enter the marks in Chemistry: "))

total = math + physics + chemistry
math_physics = math + physics

if (math >= 60 and physics >= 50 and chemistry >= 40 and total >= 200) or (math_physics >= 150):
    print("The candidate is eligible for admission.")
else:
    print("The candidate is not eligible for admission.")