import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    global val2
    total_points = 0
    print(data)

    values = data.split('mul(')
    for val in values[1:]:
        # print(val.split(","))
        val1 = val.split(",")[0]
        val2 = 0
        # for v in val.split(",")[1]:
        #     print(v)
        if val[1][0].isdigit() and val[1][1] == ")":
            val2 = val[1][0]
        elif val[1][0].isdigit() and val[1][1].isdigit() and val[1][2] == ")":
            val2 = val[0:2]
        elif val[1][0].isdigit() and val[1][1].isdigit() and val[1][2].isdigit() and val[1][3] == ")":
            val2 = val[0:3]
        print(val2)
        # mul = val1 * val2
        # total_points += mul

        # if val[0].isdigit() and val.split(",")[1][0].isdigit() and val.split(val.split(",")[1][0])[1][0] == ')':
        #     val1 = val.split(",")
        #     print(val1)

    print(values)


    return total_points


def part2(data):
    """Solve part 2."""
    total_points = 0
    lines = data.split("\n")

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
