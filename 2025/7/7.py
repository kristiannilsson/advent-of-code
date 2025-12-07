from collections import deque


with open("7.txt") as f:
    lines = f.read().splitlines()

stack = deque()
visited = set()
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        stack.append((0, i))

while stack:

    y, x = stack.pop()
    if (y, x) in visited:
        continue
    if lines[y][x] == "^":
        visited.add((y, x))
        stack.append((y, x + 1))
        stack.append((y, x - 1))
    elif y < len(lines) - 1:
        stack.append((y + 1, x))
    else:
        count += 1

print(len(visited))
