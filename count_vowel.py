text = input(" Enter some text to count the number of vowels!! :  ")
vowels = "aeiouAEIOU"
count =0
for i in text:
    if i in vowels:
        count = count +1
print(" The number of vowel in the text is :   ", count)
