# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. 
# Print the input without the spaces in the beginning.
# Example:
# Input:         Juan Dela Cruz
# Output: Juan Dela Cruz

# 1. Prompt the user to input their full name, which may include leading spaces.
fullname = str(input("Enter your full name with spaces at the beginning: "))
# 2. Use the `strip()` method to remove any leading and trailing spaces from the input.
name = fullname.lstrip()
# 3. Print the cleaned-up full name without the leading spaces.
print(name)