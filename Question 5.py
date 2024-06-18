#Design a function that takes a list of integers as input
#The function should return True if the list contains two consecutive threes (3 next to a 3) anywhere within the list.
#within the list.
#Otherwise, it should return False. For example, the function 
#should return True for [1, 3, 3] and False for [1, 3, 1, 3].

def Consecutive(lst):
    
    if len(set(lst)) != len(lst):
        return True
    # Check for consecutive integers
    sorted_lst = sorted(lst)
    return all(sorted_lst[i] == sorted_lst[i-1] for i in range(1, len(sorted_lst)))

# User input
List = input("Enter a list of integers separated by space: ")

# Convert the user input into a list of integers
lst = list(map(int, List.split()))

# Print Result
print(Consecutive(lst))




