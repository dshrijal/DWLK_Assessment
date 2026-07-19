with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40\n50\n")

with open("numbers.txt", "r") as f:
    lines = f.readlines()

numbers_list = [int(line.strip()) for line in lines]

total_sum = sum(numbers_list)
average = total_sum / len(numbers_list)

with open("result37.txt", "w") as out:
    out.write(f"Numbers: {numbers_list}\n")
    out.write(f"Sum: {total_sum}\n")
    out.write(f"Average: {average}\n")

print("Numbers read from file:", numbers_list)
print("Sum:", total_sum)
print("Average:", average)
print("Results also written to result37.txt")
