salary = float(input("Enter your salary:   "))
if salary in range(10000, 19999):
    tax = salary * 0.10
elif salary in range(20000, 39999):
    tax = salary * 0.15
elif  salary >= 40000:
    tax = salary * 0.20
else:
    tax = 0
    final_salary = salary - tax
print("The tax amount is: Rs.", tax)
print("The final salary is  : Rs.", final_salary)
