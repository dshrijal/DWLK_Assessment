amount = float(input("Enter the purchased amount: "))

if amount >= 1000:
    discount = amount * 0.05
else:
    discount = amount * 0.03

final_amount = amount - discount

print("Discount amount is :", discount)
print("Amount to pay:", final_amount)