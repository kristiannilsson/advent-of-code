grid = []

with open("6.txt") as f:
    line = f.readline()
    while line:
        line = line.replace("\n", "")
        grid.append(line)
        line = f.readline()


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return (i, j)


row, col = find_guard(grid)

direction = (0, -1)
visited = set()
visited.add((row, col))

while True:
    dx, dy = direction
    if not ((0 <= row + dy < len(grid)) and (0 <= col + dx < len(grid[row + dy]))):
        break
    if grid[row + dy][col + dx] == "#":
        direction = (-dy, dx)
        continue
    row += dy
    col += dx
    visited.add((row, col))

print(len(visited))
