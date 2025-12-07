from collections import defaultdict, deque


with open("7.txt") as f:
    lines = f.read().splitlines()

start_y = 0
start_x = None
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        start_x = i

cache = {}


def dfs(x, y):
    if lines[y][x] == "^":
        if (x, y) in cache:
            return cache[(x, y)]
        left = dfs(x + 1, y)
        right = dfs(x - 1, y)
        cache[(x, y)] = left + right
        return left + right
    elif y < len(lines) - 1:
        return dfs(x, y + 1)
    else:
        return 1


print(dfs(start_x, start_y))
