from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def is_in_bounds(self, max_x, max_y):
        return 0 <= self.x < max_x and 0 <= self.y < max_y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)


antennas = defaultdict(list)

# Read the file
with open("8.txt") as f:
    lines = f.readlines()

# Store number of lines and line length
max_y = len(lines)
max_x = len(lines[0].rstrip())  # Remove any trailing newline
print(max_x)

# Process the file
for i, line in enumerate(lines):
    for j, character in enumerate(line.rstrip()):  # Ignore trailing newline
        if character != ".":
            antennas[character].append(Point(j, i))


antinodes = set()

for key, items in antennas.items():
    for i in range(len(items)):
        print(items)
        for j in range(i + 1, len(items)):
            # print("points", items[i], items[j])
            difference = items[i] - items[j]
            first_point = items[i] + difference
            second_point = items[i]
            # print(first_point, second_point)
            while first_point.is_in_bounds(max_x, max_y) or second_point.is_in_bounds(
                max_x, max_y
            ):
                if first_point.is_in_bounds(max_x, max_y):
                    antinodes.add(first_point)
                    first_point += difference

                if second_point.is_in_bounds(max_x, max_y):
                    antinodes.add(second_point)
                    second_point -= difference


print(antinodes)

print(len(antinodes))
