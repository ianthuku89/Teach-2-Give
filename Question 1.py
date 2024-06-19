""""
Design a function that reverses the digits of an integer. 
For example, 50 should become 5 and -12 should become -21
"""
def reverse_number():
    number = int(input("Enter a number: "))
    original_number = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    print(f"Number: {original_number}")
    print(f"Reverse: {reverse}")

reverse_number()


