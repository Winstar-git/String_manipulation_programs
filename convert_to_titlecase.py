# Prog05: Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

# 1. Prompt the user to input their fullname.
fullname = input("Enter a fullname: ")
# 2. Convert the input string to lowercase using the appropriate string method.
titllecase_name = str(fullname.title())
# 3. Print the converted lowercase string as the output.
print(f"Output: {titllecase_name}")