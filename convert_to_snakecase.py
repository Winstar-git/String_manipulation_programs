# Prog10: Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

# Algorithm:
# 1. Prompt the user to input their full name in incorrect casing.
fullname = str(input("Enter a fullname: "))
# 2. Convert the input string to lower case using the  lower()` method.
name = fullname.lower()
# 3. Remove all spaces from the lower-cased string using the `replace()` method.
snake_case = name.replace(" ", "_")
# 4. Print the resulting snake case string.
print(f"Output: {snake_case}")