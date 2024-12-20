import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(cards):
    total_points = 0
    lines = cards.split("\n")
    for l in lines:
        card_no = (l.split(":")[0]).split(" ")[1]
        # Split the card into winning numbers and numbers you have
        left = (l.split(" | ")[0]).split(":")[1]
        right = l.split(" | ")[1]
        winning_numbers = set(map(int, left.split()))
        your_numbers = list(map(int, right.split()))
        # print(winning_numbers, your_numbers)

        # Determine matches and calculate points
        points = 0
        for i, num in enumerate(your_numbers):
            if num in winning_numbers:
                if points == 0:
                    points = 1  # First match gives 1 point
                else:
                    points *= 2  # Each subsequent match doubles the points

        total_points += points

    return total_points


def part2(data):
    """Solve part 2."""
    p2 = 0
    return p2


def solve(io):
    """Solve the puzzle for the given input."""
    data = parse(io)
    # print(data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = "C:\\Users\\Arun\\Documents\\Arun\\arundataengineering\\AoC\\2023\\input.txt"
    print(f"{path}")
    puzzle_input = pathlib.Path(path).read_text().strip().lstrip()
    # print(puzzle_input)
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
