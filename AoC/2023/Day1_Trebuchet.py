import pathlib


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    """Solve part 1."""
    p1 = 0
    for line in data.split('\n'):
        p1_digits = []
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
        p1 += int(p1_digits[0] + p1_digits[-1])
    return p1


def part2(data):
    """Solve part 2."""
    p2 = 0
    for line in data.split('\n'):
        p1_digits = []
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p2_digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_digits.append(str(d + 1))
        p2 += int(p2_digits[0] + p2_digits[-1])
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
