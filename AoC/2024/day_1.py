import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(cards):
    total_points = 0
    left_list, right_list = [] , []
    lines = cards.split("\n")
    for l in lines:
        left_list.append(int(l.split(" ")[0]))
        right_list.append(int(l.split("  ")[1].lstrip()))
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i in range(len(left_list)):
        if left_list[i] > right_list[i]:
            total_points += left_list[i] - right_list[i]
        else:
            total_points += right_list[i] - left_list[i]

    return total_points


def part2(data):
    """Solve part 2."""
    total_points = 0
    left_list, right_list = [], []
    lines = data.split("\n")
    for l in lines:
        left_list.append(int(l.split(" ")[0]))
        right_list.append(int(l.split("  ")[1].lstrip()))
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i in range(len(left_list)):
        temp_count = right_list.count(left_list[i])
        total_points += left_list[i] * temp_count
        temp_count = 0
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
