lines = []
with open("9.txt") as f:
    for line in f.read().splitlines():
        if not line:
            continue
        lines.append(tuple(map(int, line.split(","))))

edges = []
n = len(lines)
for i in range(n):
    p1 = lines[i]
    p2 = lines[(i + 1) % n]
    edges.append((p1, p2))


def is_between(c, a, b):
    return min(a, b) < c < max(a, b)


def intervals_overlap(a1, a2, b1, b2):
    return max(min(a1, a2), min(b1, b2)) < min(max(a1, a2), max(b1, b2))


def is_point_inside(px, py, edges):
    crossings = 0
    for p1, p2 in edges:
        if p1[0] == p2[0]:
            edge_x = p1[0]
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

            if edge_x > px and y_min <= py < y_max:
                crossings += 1
    return crossings % 2 == 1


max_area = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = lines[i]
        x2, y2 = lines[j]

        rx_min, rx_max = min(x1, x2), max(x1, x2)
        ry_min, ry_max = min(y1, y2), max(y1, y2)

        area = (rx_max - rx_min + 1) * (ry_max - ry_min + 1)
        if area <= max_area:
            continue
        edge_hit = False
        for p1, p2 in edges:
            if p1[0] == p2[0]:
                edge_x = p1[0]
                if rx_min < edge_x < rx_max:
                    if intervals_overlap(p1[1], p2[1], ry_min, ry_max):
                        edge_hit = True
                        break
            elif p1[1] == p2[1]:
                edge_y = p1[1]
                if ry_min < edge_y < ry_max:
                    if intervals_overlap(p1[0], p2[0], rx_min, rx_max):
                        edge_hit = True
                        break

        if edge_hit:
            continue

        cx = (rx_min + rx_max) / 2
        cy = (ry_min + ry_max) / 2
        if not is_point_inside(cx, cy, edges):
            continue

        max_area = area

print(max_area)
