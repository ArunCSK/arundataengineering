import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    """Solve part 1."""
    p1 = 0
    lines = data.split('\n')
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    nums = defaultdict(list)
    for r in range(len(G)):
        gears = set()  # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for c in range(len(G[r]) + 1):
            if c < C and G[r][c].isdigit():
                n = n * 10 + int(G[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < R and 0 <= c + cc < C:
                            ch = G[r + rr][c + cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch == '*':
                                gears.add((r + rr, c + cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()
    return p1


def part2(data):
    """Solve part 2."""
    p2 = 0
    p1 = 0
    lines = data.split('\n')
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    nums = defaultdict(list)
    for r in range(len(G)):
        gears = set()  # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for c in range(len(G[r]) + 1):
            if c < C and G[r][c].isdigit():
                n = n * 10 + int(G[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < R and 0 <= c + cc < C:
                            ch = G[r + rr][c + cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch == '*':
                                gears.add((r + rr, c + cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()
    for k, v in nums.items():
        if len(v) == 2:
            p2 += v[0] * v[1]
    return p2


def solve(io):
    """Solve the puzzle for the given input."""
    data = parse(io)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    path = "C:\\Users\\Arun\\Documents\\Arun\\arundataengineering\\AoC\\2023\\input.txt"
    print(f"{path}")
    puzzle_input = pathlib.Path(path).read_text().strip().lstrip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
