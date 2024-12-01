import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    """Solve part 1."""
    p1 = 0
    for line in data.split('\n'):
        ok = True
        id_, line = line.split(':')
        V = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                n = int(n)
                V[color] = max(V[color], n)
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False
        if ok:
            p1 += int(id_.split()[-1])
    return p1


def part2(data):
    """Solve part 2."""
    p2 = 0
    for line in data.split('\n'):
        ok = True
        id_, line = line.split(':')
        V = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                n = int(n)
                V[color] = max(V[color], n)
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False
        score = 1
        for v in V.values():
            score *= v
        p2 += score

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
    puzzle_input = pathlib.Path(path).read_text().strip().lstrip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
