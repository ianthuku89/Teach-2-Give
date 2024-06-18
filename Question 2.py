#Write a recursive function to calculate the factorial of a number
def factorial(num): 
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter Number: "))
factorial_result = factorial(num)

print(f"Number: {num}")
print(f"Factorial: {factorial_result}")
