with open("12.txt") as f:
    lines = f.read().splitlines()

expected_index = 0
shapes = []
sizes = []
i = 0
shape_area = 0
while lines[i] == "" or "x" not in lines[i]:
    if expected_index == len(shapes):
        shapes.append([])
    if lines[i] == "":
        i += 1
        sizes.append(shape_area)
        shape_area = 0
        continue
    if lines[i][0] == "#" or lines[i][0] == ".":
        for char in lines[i]:
            if char == "#":
                shape_area += 1
        shapes[expected_index].append(lines[i])
    elif lines[i][0:2] != str(expected_index) + ":":
        expected_index += 1
    i += 1
regions = []
while i < len(lines):
    parts = lines[i].split(":")
    size = tuple(map(int, parts[0].split("x")))
    gifts = tuple(map(int, parts[1].strip().split(" ")))
    regions.append((size, gifts))
    i += 1

count = 0
for size, gifts in regions:
    grid_size = size[0] * size[1]
    gift_area = 0
    presents = 0
    for i in range(len(gifts)):
        presents += gifts[i]
        gift_area += gifts[i] * sizes[i]

    if grid_size < gift_area:
        continue
    count += 1
print(count)
