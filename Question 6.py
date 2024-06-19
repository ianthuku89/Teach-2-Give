""""
Master Yoda, a renowned Jedi Master from the Star Wars universe, is known 
for his unique way of speaking. He often reverses the order of words in his 
sentences. For example, instead of saying "I am home" he might say "Home 
am I" Design a function that takes a sentence as input and returns a new 
sentence with the words reversed in the same order that Master Yoda would 
use

"""

def reverse_words(sentence):
  
  reversed_sentence = ' '.join(sentence.split()[::-1])
  return reversed_sentence

# User input
Input = input("Enter the sentence you wish to reverse: ")

# Print the reversed sentence
reversed_words = reverse_words(Input)
print(reversed_words)



