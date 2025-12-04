with open("3.txt") as f:
    directions = f.readline()


directions_map = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def update_visited(directions, visited):
    x_pos = 0
    y_pos = 0
    for direction in directions:
        dx, dy = directions_map[direction]
        x_pos += dx
        y_pos += dy
        visited.add((x_pos, y_pos))


visited = set([(0, 0)])

update_visited(directions, visited)

print(len(visited))

santa = directions[::2]
robo_santa = directions[1::2]
visited = set([(0, 0)])

update_visited(santa, visited)
update_visited(robo_santa, visited)

print(len(visited))
