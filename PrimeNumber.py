""" check prime number
take number from user
   input:7 
   output: is prime

"""
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Is prime")
else:
    print("Not a prime number")