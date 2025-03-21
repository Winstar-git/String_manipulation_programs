# Prog04: Create a program that ask the user to input their fullname. 
# Print the input in all lower case.
# Example:
# Input: Juan Dela Cruz
# Output: juan dela cruz

# 1. Prompt the user to input their fullname.
fullname = input("Enter a fullname: ")
# 2. Convert the input string to lowercase using the appropriate string method.
lowercase_name = str(fullname.lower())
# 3. Print the converted lowercase string as the output.
print(f"Output: {lowercase_name}")