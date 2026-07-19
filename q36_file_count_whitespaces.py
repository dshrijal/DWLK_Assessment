


with open("sample.txt", "w") as f:
    f.write("Hello World. This is a simple text file.\nPython is fun to learn.\n")

with open("sample.txt", "r") as f:
    text = f.read()

whitespace_count = 0
for ch in text:
    if ch.isspace():       
        whitespace_count += 1

print("Number of whitespaces:", whitespace_count)
