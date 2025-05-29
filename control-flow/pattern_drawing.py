size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing stars
    row += 1  # Increment the row counter