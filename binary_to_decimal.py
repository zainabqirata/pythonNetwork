def bin_to_dec(input):
    try:
        return int(input, 2)
    except ValueError:
        return None

# Read binary number input from user
input = input("Enter a binary number: ")

# Check for valid binary input
if not all(char in '01' for char in input):
    print("Invalid input.")
else:
    # Convert to decimal and display the result
    dec_num = bin_to_dec(input)
    
    if dec_num is not None:
        print(f" {input} is {dec_num}")
    else:
        print("Invalid binary number.")
