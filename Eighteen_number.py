def find_smallest_and_largest(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest



numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

smallest, largest = find_smallest_and_largest(numbers)
print(f"\nList of numbers: {numbers}")
print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")