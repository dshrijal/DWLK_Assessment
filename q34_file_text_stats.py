
with open("sample.txt", "w") as f:
    f.write("Hello World. This is a simple text file.\nPython is fun to learn.\n")

with open("sample.txt", "r") as f:
    text = f.read()

num_characters = len(text)

vowels = "aeiouAEIOU"
num_vowels = 0
num_consonants = 0

for ch in text:
    if ch.isalpha():        
        if ch in vowels:
            num_vowels += 1
        else:
            num_consonants += 1

words = text.split()       
num_words = len(words)

lines = text.split("\n")
num_lines = len(lines)

print("Number of characters:", num_characters)
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
