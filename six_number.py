Balance = float(input("Enter the balance amount: "))
if Balance >= 99999:
    interest = Balance * 0.07
elif Balance >= 50000:
    interest = Balance * 0.05
else:
    interest = Balance * 0.03
print("Interest amount is :" ,interest)
print("The total amount is :" , Balance + interest)

