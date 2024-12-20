import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    total_points = 0
    grid = data.split('\n')
    word = "XMAS"
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    # print(rows, cols)

    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-right diagonal
        (-1, -1),  # Up-left diagonal
        (1, -1),  # Down-left diagonal
        (-1, 1),  # Up-right diagonal
    ]

    def is_valid(x, y):
        """Check if a coordinate is within the grid."""
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        """Check if the word exists starting from (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    # Traverse each cell of the grid
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    total_points += 1

    return total_points


def part2(data):
    """Solve part 2."""
    total_points = 0
    grid = data.split('\n')
    rows = len(grid)
    cols = len(grid[0])
    # print(grid[1][1])

    def is_valid(x, y):
        """Check if a coordinate is within the grid."""
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y):
        """Check if an X-MAS pattern exists with (x, y) as the center 'A'."""
        count = 0
        # Forward MAS diagonals
        if (is_valid(x - 1, y - 1) and grid[x - 1][y - 1] == 'M' and
                is_valid(x + 1, y + 1) and grid[x + 1][y + 1] == 'S' and
                is_valid(x - 1, y + 1) and grid[x - 1][y + 1] == 'S' and
                is_valid(x + 1, y - 1) and grid[x + 1][y - 1] == 'M'):
            count += 1

        if (is_valid(x - 1, y - 1) and grid[x - 1][y - 1] == 'M' and
                is_valid(x + 1, y + 1) and grid[x + 1][y + 1] == 'S' and
                is_valid(x - 1, y + 1) and grid[x - 1][y + 1] == 'M' and
                is_valid(x + 1, y - 1) and grid[x + 1][y - 1] == 'S'):
            count += 1

        # Reverse MAS diagonals
        if (is_valid(x - 1, y - 1) and grid[x - 1][y - 1] == 'S' and
                is_valid(x + 1, y + 1) and grid[x + 1][y + 1] == 'M' and
                is_valid(x - 1, y + 1) and grid[x - 1][y + 1] == 'M' and
                is_valid(x + 1, y - 1) and grid[x + 1][y - 1] == 'S'):
            count += 1

        # Reverse MAS diagonals
        if (is_valid(x - 1, y - 1) and grid[x - 1][y - 1] == 'S' and
                is_valid(x + 1, y + 1) and grid[x + 1][y + 1] == 'M' and
                is_valid(x - 1, y + 1) and grid[x - 1][y + 1] == 'S' and
                is_valid(x + 1, y - 1) and grid[x + 1][y - 1] == 'M'):
            count += 1
        return count

    # Traverse each cell of the grid
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 'A':
                # print(grid[x][y])
                total_points += check_word(x, y)

    return total_points


def solve(io):
    """Solve the puzzle for the given input."""
    data = parse(io)
    # print(data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = "C:\\Users\\Arun\\Documents\\Arun\\arundataengineering\\AoC\\2024\\input.txt"
    print(f"{path}")
    puzzle_input = pathlib.Path(path).read_text().strip().lstrip()
    # print(puzzle_input)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
