# Prog06: Create a program that ask the user to input their fullname in incorrect casing. 
# Print each character of the input in reverse casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuaN deLA cRuz

# 1. Prompt the user to input their fullname.
fullname = input("Enter a fullname: ")
# 2. Convert the input string and  use the swapcase() to reverse the case of each character.
reverse_case_name = str(fullname.swapcase())
# 3. Print the reverse case string as the output.
print(f"Output: {reverse_case_name}")