# Prog03: Create a program that ask the user to input their fullname. 
# Print the input in all capital letter.
# Example:
# Input: Juan Dela Cruz
# Output: JUAN DELA CRUZ

# 1. Prompt the user to input their fullname.
fullname = input("Enter a fullname: ")
# 2. Convert the input string to uppercase using the appropriate string method.
uppercase_name = str(fullname.upper())
# 3. Print the converted uppercase string as the output.
print(f"Output: {uppercase_name}")