def count_diagonals(n):
    diagonals = n * (n - 3) // 2
    return diagonals
num_sides = int(input())

diagonals_count = count_diagonals(num_sides)
print(diagonals_count)
