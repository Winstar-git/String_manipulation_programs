# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. 
# Add zeros at the beginning to complete the 6 digit.
# Example:
# Input: 143
# Output: 000143

# 1. Start a while loop.
while True:
    try:
# 2. Prompt the user to input a number (0-1000).
        number = int(input("Enter a number (0-1000): "))
# 3. Limit the input number from 0-1000
        if 0 <= number <= 1000:
# 4. If valid, print the number in 6-digit format (padded with leading zeros) and break the loop.
            print(f"Output: {number:06}")
            break
# 5. If invalid, display an error message asking for a number between 0 and 1000.
        else:
            print('Invalid input. Please enter a number between 0 and 1000.')

# 6. If the input is not a valid integer, catch the ValueError and display an error message.
    except ValueError:
        print("Invalid input. Please enter valid number.")
# 7. Repeat the loop until a valid input is provided.
