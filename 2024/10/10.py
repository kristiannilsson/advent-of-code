with open("10.txt") as f:
    grid = [line.replace("\n", "") for line in f]


def climb(i, j):
    stack = [(i, j, 0)]
    visited = set()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    total_tracks = 0
    while stack:
        row, col, current_value = stack.pop()
        next_value = current_value + 1
        if current_value == 9:
            total_tracks += 1
            visited.add((row, col))
        for dx, dy in directions:
            new_row = row + dy
            new_col = col + dx
            if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[row])):
                continue
            if (
                grid[new_row][new_col] != "."
                and int(grid[new_row][new_col]) == next_value
            ):
                stack.append((new_row, new_col, next_value))
    return len(visited), total_tracks


total_score = 0
total_distinct_score = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "0":
            score, distinct_score = climb(i, j)
            total_score += score
            total_distinct_score += distinct_score

print(total_score, total_distinct_score)
