import time

start = time.perf_counter()

lines = []
with open("9.txt") as f:
    for line in f.read().splitlines():
        raw_coordinates = line.split(",")
        coordinates = map(int, raw_coordinates)
        lines.append(tuple(coordinates))

lines.sort()  # Sort by x, then y


def is_inside_square(x1, y1, x2, y2, x_to_check, y_to_check):
    if not (x1 <= x_to_check <= x2):
        return False
    return y1 <= y_to_check <= y2


largest_rectangle = ((-float("inf"), -float("inf")), (float("inf"), float("inf")))
largest_area = 0

for i in range(len(lines)):
    x1, y1 = lines[i]

    corner1, corner2 = largest_rectangle
    if not is_inside_square(corner1[0], corner1[1], corner2[0], corner2[1], x1, y1):
        continue
    for j in range(i + 1, len(lines)):
        x2, y2 = lines[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > largest_area:
            largest_rectangle = ((x1, y1), (x2, y2))
            largest_area = area


print(largest_area)
end = time.perf_counter()
print(f"Execution time: {end - start} seconds")
