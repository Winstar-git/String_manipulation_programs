# Prog07: Create a program that ask the user to input a complete statement. 
# Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

# Algorithm:
# 1. Prompt the user to input a complete statement.
statement = str(input("Enter statement: "))
# 2. Split the input statement into words using whitespace as the delimiter.
split_statement = statement.split()
# 3. Count the number of words in the resulting list.
count_statement = len(split_statement)
# 4. Print the total word count.
print(f"Output: {count_statement}")
