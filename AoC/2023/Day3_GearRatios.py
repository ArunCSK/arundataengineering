import pathlib
from collections import defaultdict


path = "C:\\Users\\Arun\\Documents\\Arun\\dbrx_instruct\\DSA\\AoC\\2023\\input.txt"
print(f"{path}")
schematic = pathlib.Path(path).read_text().strip().lstrip()

# print(schematic)

# Convert to a 2D list for easier processing
grid = [list(row) for row in schematic]

# Directions for adjacency: vertical, horizontal, and diagonal
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# Function to check if a cell is a symbol
def is_symbol(cell):
    return cell in "*#$+"


# Function to check if a number is adjacent to a symbol
def is_part_number(grid, row, col):
    if not grid[row][col].isdigit():
        return False  # Not a number

    # Check all adjacent cells
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):  # Bounds check
            if is_symbol(grid[nr][nc]):
                return True
    return False


# Calculate the sum of all part numbers
part_sum = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if is_part_number(grid, r, c):
            part_sum += int(grid[r][c])

print(part_sum)
