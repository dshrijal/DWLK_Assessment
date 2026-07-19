
with open("sample.txt", "w") as f:
    f.write("Hello World. This is a simple text file.\nPython is fun to learn.\n")

with open("sample.txt", "r") as f:
    text = f.read()

num_letters = 0
num_digits = 0
num_others = 0

for ch in text:
    if ch.isalpha():
        num_letters += 1
    elif ch.isdigit():
        num_digits += 1
    else:
        num_others += 1

with open("output35.txt", "w") as out:
    out.write(f"Number of letters: {num_letters}\n")
    out.write(f"Number of digits: {num_digits}\n")
    out.write(f"Number of other characters: {num_others}\n")

print("Done! Results have been written to output35.txt")
print(f"(letters: {num_letters}, digits: {num_digits}, others: {num_others})")
