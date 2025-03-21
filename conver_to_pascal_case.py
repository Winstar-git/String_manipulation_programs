# Prog09: Create a program that ask the user to input their fullname in incorrect casing. 
# Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

# Algorithm:
# 1. Prompt the user to input their full name in incorrect casing.
fullname = str(input("Enter a fullname: "))
# 2. Convert the input string to title case using the `title()` method.
name = fullname.title()
# 3. Remove all spaces from the title-cased string using the `replace()` method.
pascal_case = name.replace(" ","")
# 4. Print the resulting PascalCase string.
print(f"Output: {pascal_case}")