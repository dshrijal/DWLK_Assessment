number = input("Enter a number :  ")
if number == number[::-1]: # This is called string slicing, creates a reversed copy of the string.
    print(" The number is a palindrome number")
else:
    print("Please Try again, It is'nt a palindrome number")

