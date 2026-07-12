number = int(input("Enter a number to check if it is prime number or not: "))
if number > 1: # checks if the user input is greater than 1 or not  if greater than 1 then it will check for prime or not!!
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:

            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")