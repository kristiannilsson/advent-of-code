from collections import deque

WIDTH = 71
HEIGHT = 71
bytes = []


with open("18.txt") as f:
    for line in f:
        byte = tuple(map(int, line.strip().split(",")))
        bytes.append(byte)


def generate_blocked_tiles():
    blocked_tiles = []
    current_blocked = set()

    for x, y in bytes:
        current_blocked.add((x, y))
        blocked_tiles.append(current_blocked.copy())
    return blocked_tiles


tiles = generate_blocked_tiles()


def find_path(blocked_tiles):
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        d, x, y = queue.pop()
        if x == WIDTH - 1 and y == HEIGHT - 1:
            return d
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= ny < WIDTH and 0 <= nx < HEIGHT):
                continue
            if (nx, ny) in blocked_tiles or (nx, ny) in visited:
                continue
            queue.appendleft((d + 1, nx, ny))
            visited.add((nx, ny))
    return None


left, right = 1023, len(bytes) - 1
while left < right:
    guess = (left + right) // 2
    if find_path(tiles[guess]):
        left = guess
    else:
        right = guess - 1
print(find_path(tiles[1023]))
print(bytes[guess])
