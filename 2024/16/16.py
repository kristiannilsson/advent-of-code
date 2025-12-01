from collections import deque
from heapq import heappop, heappush


with open("16.txt") as f:
    grid = [list(line) for line in f]


def find_starting_point(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                return x, y
    return None


def get_distances(start_x, start_y):
    distances = {}
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            distances[(x, y)] = {key: float("inf") for key in directions}
    distances[(start_x, start_y)][(1, 0)] = 0
    return distances


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = find_starting_point(grid)
distances = get_distances(x, y)
queue = []
heappush(queue, (0, x, y, (1, 0), [(x, y)]))
tiles = {(x, y)}
lowest_cost = float("inf")
while queue:
    cost, x, y, direction, path = heappop(queue)
    if grid[y][x] == "E":
        if cost < lowest_cost:
            lowest_cost = cost
            tiles = {(x, y)}
        if cost == lowest_cost:
            tiles.update(path)
    for dx, dy in directions:
        new_cost = cost + 1
        nx, ny = x + dx, y + dy
        if grid[ny][nx] == "#":
            continue
        direction_x, direction_y = direction
        if (dx, dy) == (-direction_x, -direction_y):
            continue
        if (dx, dy) != (direction_x, direction_y):
            new_cost += 1000

        if new_cost > distances[(nx, ny)][(dx, dy)]:
            continue

        distances[(nx, ny)][(dx, dy)] = new_cost
        heappush(queue, (new_cost, nx, ny, (dx, dy), path + [(x, y)]))
print(lowest_cost, len(tiles))
