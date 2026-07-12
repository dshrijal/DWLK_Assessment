for numbers in range (2, 101):
    for i in range(2,int(numbers**0.5)+1):
        if numbers % i ==0:
            break
    else:
          print(numbers)

            