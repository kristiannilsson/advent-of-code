grid = []

with open("6.txt") as f:
    line = f.readline()
    while line:
        line = line.replace("\n", "")
        grid.append(list(line))
        line = f.readline()


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j


def traverse(row, col, direction):
    dx, dy = direction
    if not ((0 <= row + dy < len(grid)) and (0 <= col + dx < len(grid[row + dy]))):
        return None, None, None
    if grid[row + dy][col + dx] == "#":
        direction = (-dy, dx)
        dx, dy = direction
    row += dy
    col += dx
    return row, col, direction


direction = (0, -1)
row, col = find_guard(grid)
visited = set((row, col))
visited.add((row, col))

while True:
    row, col, direction = traverse(row, col, direction)
    if row is None:
        break
    visited.add((row, col))

row, col = find_guard(grid)
cycle_count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(i, j)
        if row == i and col == j:
            continue
        is_cycle = True
        direction = (0, -1)
        original_value = grid[i][j]
        grid[i][j] = "#"
        slow = traverse(row, col, direction)
        fast = traverse(*traverse(row, col, direction))
        while slow != fast:
            slow = traverse(*slow)
            fast = traverse(*fast)
            if fast[0] is None:
                is_cycle = False
                break
            fast = traverse(*fast)
            if fast[0] is None:
                is_cycle = False
                break
        if original_value != "#":
            grid[i][j] = "."
        if is_cycle:
            cycle_count += 1
# print(len(visited))
print("cycles", cycle_count)
