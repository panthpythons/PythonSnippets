""" To print prime number from given range"""
# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop through each number in the range
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # If a divisor is found, break without printing anything
                break
        else:
            # If no divisors were found, print the number as it is prime
            print("Prime number:", num)