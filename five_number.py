amount = float(input("Enter the purchased amount: "))

if amount >= 5000:
    discount = amount * 0.1
   
elif amount >= 4000:
    discount = amount * 0.07

elif amount>=3000:
    discount = amount * 0.05

elif amount >= 2000:
    discount = amount * 0.03
else:
    discount =  amount * 0.02

final_amount = amount - discount
print("Purchased Amount Is : Rs.", amount)
print("Discounted Amount Is : Rs.",discount)
print("Final Amount is: Rs.", final_amount)