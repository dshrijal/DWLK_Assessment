def Even_Or_Odd_NUmber(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num %2 ==0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers
num = int(input("Enter a number: "))
even_numbers, odd_numbers = Even_Or_Odd_NUmber(range(1, num+1))
print(f"Even numbers from 1 to {num}: {even_numbers}")
print(f"Odd numbers from 1 to {num}: {odd_numbers}")

