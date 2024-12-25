import pathlib
from collections import defaultdict, deque


def parse(io):
    """Parse input."""
    data = io
    return data


def part1(data):
    total_points = 0
    page_order, page_update = data.split("\n\n")
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


def build_graph(rules):
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph


def is_valid_order(update, graph):
    position = {page: i for i, page in enumerate(update)}
    for x in update:
        for y in graph[x]:
            if y in position and position[x] > position[y]:
                return False
    return True

def topological_sort(update, graph):
    indegree = {page: 0 for page in update}
    for x in update:
        for y in graph[x]:
            if y in indegree:
                indegree[y] += 1

    queue = deque([node for node in update if indegree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            if neighbor in indegree:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

    return sorted_order
def part2(data):
    """Solve part 2."""
    total_points = 0
    sections = data.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    graph = build_graph(rules)
    fix_invalid = True
    for update in updates:
        if not is_valid_order(update, graph):
            if fix_invalid:
                update = topological_sort(update, graph)
        else:
            if not fix_invalid:
                middle_page = update[len(update) // 2]
                total_points += middle_page

    if fix_invalid:
        for update in updates:
            if not is_valid_order(update, graph):
                update = topological_sort(update, graph)
                middle_page = update[len(update) // 2]
                total_points += middle_page

    # print(graph)

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
