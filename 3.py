amount = float(input("enter the amount:"))
if amount >= 1000:
    discount = amount * 0.05
    final_amount = amount - discount
    print(" The amount after discount  is :", final_amount)
else:
    print(" shop more than 1000 to get discount")


