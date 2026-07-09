math = float(input("Enter the obtained marks in mathematics: "))
physics = float(input("Enter the obtained marks in physics: "))
chemistry = float(input("Enter the obtained marks in chemistry: "))
add=math + physics + chemistry
if math >=60 and physics >= 50 and chemistry >= 40 and add >= 200:
    print("The student has passed in all subjects and got admission in our institute.")
else:
    print("The student is not eligible for admission.")