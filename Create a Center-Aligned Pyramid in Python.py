# Prompt the user to enter the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Iterate over each row of the pyramid
for i in range(1, height + 1):
    # Print spaces for the left side to center the pyramid
    print(" " * (height - i), end="")
    # Print stars for the current row, increasing with each row
    print("*" * (2 * i - 1))
