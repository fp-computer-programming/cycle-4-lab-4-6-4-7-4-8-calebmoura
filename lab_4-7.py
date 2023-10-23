# Author: caleb moura

# Prompt user for 5 numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")
num5 = input("Enter the fifth number: ")

# Store numbers as a single string
num_string = f'{num1} {num2} {num3} {num4} {num5}'

# Print string
print(f'Numbers entered: {num_string}')

# Extract the smallest and largest numbers
numbers = [int(num) for num in num_string.split()]
smallest = min(numbers)
largest = max(numbers)

# Print the smallest and largest numbers
print(f'The smallest number given was {smallest}')
print(f'The largest number given was {largest}')

# Calculate product
product = smallest * largest

# Print result, "product"
print(f'The product of the two numbers extracted was {product}')