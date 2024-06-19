"""
Design a function that takes a string or sequence of characters as input
and returns the character that appears most frequently.
//Eg 11189 => '1'
//hello => l
"""
def frequent_char(input_str):
    max_count = 0
    most_frequent_char = None
    for char in input_str:
        count = input_str.count(char)
        if count > max_count:
            max_count = count
            most_frequent_char = char
    return most_frequent_char

user_input = input("Enter a string or characters: ")
result = frequent_char(user_input)
print(result)
