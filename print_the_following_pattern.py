n = int(input())  # Get user input for number of rows

# Iterate over numbers from 1 to n
for i in range(1, n+1):
    # Iterate over numbers from 1 to i, and print each number
    for j in range(1, i+1):
        print(j, end="")
    print()  # Move to next line after printing each row
