import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    total_points = 0
    page_order , page_update = data.split("\n\n")
    # Parse ordering rules
    rules = []
    for line in page_order.splitlines():
        X, Y = map(int, line.split("|"))
        rules.append((X, Y))

    updates = []
    for line in page_update.splitlines():
        updates.append(list(map(int, line.split(","))))

    def is_valid(update, rules):
        page_index = {page: idx for idx, page in enumerate(update)}  # Map page to its index in the update
        for x, y in rules:
            if x in page_index and y in page_index:
                if page_index[x] > page_index[y]:
                    return False
        return True

    """Check if the update respects the given ordering rules."""
    for update in updates:
        if is_valid(update, rules):
            total_points += update[len(update) // 2]

    return total_points


def part2(data):
    """Solve part 2."""
    total_points = 0


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
