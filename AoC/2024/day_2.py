import pathlib
from collections import defaultdict


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    total_points = 0
    lines = data.split("\n")
    for l in lines:
        reports = list(map(int, l.split()))
        """Check if a single report is safe."""
        differences = [reports[i + 1] - reports[i] for i in range(len(reports) - 1)]

        # Check for monotonicity and valid differences
        is_increasing = all(0 < diff <= 3 for diff in differences)
        is_decreasing = all(-3 <= diff < 0 for diff in differences)

        if is_increasing or is_decreasing:
            total_points += 1

    return total_points


def is_safe_report(report):
    """Check if a single report is safe."""
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check for monotonicity and valid differences
    is_increasing = all(0 < diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff < 0 for diff in differences)

    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    """Check if a report can be made safe by removing one level."""
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe_report(modified_report):
            return True
    return False


def part2(data):
    """Solve part 2."""
    total_points = 0
    modified_reports = []
    lines = data.split("\n")
    for line in lines:
        xs1 = list(map(int, line.split()))

        good = False
        for j in range(len(xs1)):
            xs = xs1[:j] + xs1[j + 1:]
            if is_good(xs):
                good = True
        if good:
            total_points += 1

    return total_points


def is_good(xs):
    inc_or_dec = (xs == sorted(xs) or xs == sorted(xs, reverse=True))
    ok = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not 1 <= diff <= 3:
            ok = False
    return inc_or_dec and ok


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
