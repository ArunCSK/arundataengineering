import pathlib


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    """Solve part 1."""
    p1 = 0
    return p1


def part2(data):
    """Solve part 2."""
    p2 = 0
    return p2


def solve(io):
    """Solve the puzzle for the given input."""
    data = parse(io)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = "C:\\Users\\Arun\\Documents\\Arun\\dbrx_instruct\\DSA\\AoC\\2023\\input.txt"
    print(f"{path}")
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
