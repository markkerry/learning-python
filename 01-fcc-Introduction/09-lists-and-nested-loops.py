# 4 rows and 3 columns
number_grid = [
    [1, 2, 3], # row 1 in index position 0
    [4, 5, 6], # row 2 in index position 1
    [7, 8, 9],
    [0]
]

# To get the "1" we'll need row 0, column 0
print(number_grid[0][0])

# To get the "9" we'll need row 2, column 2
print(number_grid[2][2])

# To get the "0" we'll need row 3, column 0
print(number_grid[3][0])

# Nested loop to get every column and row in the grid
for row in number_grid:
    for col in row:
        print(col)
