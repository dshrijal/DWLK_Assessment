salary = float(input("Enter your gross salary: "))

if salary < 10000:
    tax = 0
elif salary <= 19999:
    tax = salary * 0.10
elif salary <= 39999:
    tax = salary * 0.15
else:
    tax = salary * 0.20

net_salary = salary - tax

print("Gross Salary: Rs.", salary)
print("Tax: Rs.", tax)
print("Net Salary: Rs.", net_salary)