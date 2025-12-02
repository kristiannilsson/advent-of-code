from collections import defaultdict


with open("12.txt") as f:
    grid = [line.replace("\n", "") for line in f]


def explore_region(i, j):
    stack = [(i, j)]
    c = grid[i][j]
    visited.add((i, j))
    perimeter = 0
    area = 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while stack:
        row, col = stack.pop()
        local_perimeter = 4
        for dx, dy in directions:
            new_row = row + dy
            new_col = col + dx
            if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row])):
                continue
            if grid[new_row][new_col] == c:
                local_perimeter -= 1
            else:
                continue
            if (new_row, new_col) in visited:
                continue
            visited.add((new_row, new_col))
            stack.append((new_row, new_col))
            area += 1
        perimeter += local_perimeter
    print(c, perimeter)
    return area * perimeter


visited = set()
total = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) in visited:
            continue
        total += explore_region(i, j)
print(total)
