def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Input: Prompt the user to enter a non-negative integer
number = int(input("Enter a non-negative integer: "))

# Calculate the factorial of the input number
result = calculate_factorial(number)

# Output: Display the result
print(f"The factorial of {number} is {result}")
