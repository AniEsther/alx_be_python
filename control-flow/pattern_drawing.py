size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Outer loop using while (for rows)
while row < size:
    # Inner loop using for (for columns)
    for col in range(size):
        print("*", end="")  # print * on the same line
    print()  # move to the next line after each row
    row += 1