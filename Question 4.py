#Design a function that determines whether a given string is a pangram
#A pangram is a sentence or phrase containing every letter of the alphabet at 
#least once. 
# Punctuation and case are typically ignored For example, the 
#string "The quick brown fox jumps over the lazy dog" is a pangram, while 
#"Hello, world!" is not.

def checkPangram(s):
    present = [False] * 26

    # Iterate over the sentence
    for c in s.lower():
        if c.isalpha():
            present[ord(c) - ord('a')] = True
    return all(present)

# User input
sentence = input("Enter the sentence to check for pangram: ")

# Check if it's a pangram
if checkPangram(sentence):
    print('"{}"'.format(sentence))
    print("\n The sentence is a pangram")
else:
    print('"{}"'.format(sentence))
    print("\nThe sentence is not a pangram")

