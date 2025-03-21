# Prog08: Create a program that ask the user to input their fullname. 
# Print the number of characters in the input.
# Example:
# Input: Juan Dela Cruz
# Output: 14

# Algorithm:
# 1. Prompt the user to input a complete statement.
fullname = str(input("Enter a fullname: "))
# 3. Count the number of words in the resulting list including spaces.
count_characters = len(fullname) 
# 4. Print the total word count.
print(f"Output: {count_characters}")