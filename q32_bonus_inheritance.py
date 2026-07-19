
class Bonus:
    def __init__(self, sales_id, sales_amount):
        self.sales_id = sales_id
        self.sales_amount = sales_amount

    def get_bonus(self):
        return self.sales_amount * 0.05

class PremiumBonus(Bonus):   
    def get_premium_bonus(self):
        return self.sales_amount * 0.05 + (self.sales_amount - 2500) * 0.01

p1 = PremiumBonus("S101", 5000)

print("Sales ID:", p1.sales_id)
print("Regular Bonus:", p1.get_bonus())
print("Premium Bonus:", p1.get_premium_bonus())
