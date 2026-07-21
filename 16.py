number = int(input("Enter a number: "))

original = number
num_digits = len(str(number))
sum_of_powers = 0

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number = number // 10

if sum_of_powers == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is not an Armstrong Number")