import heapq
import math

with open("8.txt") as f:
    lines = f.read().splitlines()

coordinates = []

for line in lines:
    raw_coordinates = map(int, line.split(","))
    coordinates.append(tuple(raw_coordinates))
coordinates.sort()


def distance(coordinate, other_coordinate):
    x1, y1, z1 = coordinate
    x2, y2, z2 = other_coordinate
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def find_closest_coordinate(coordinate, coordinates):
    lowest_distance = float("inf")
    closest_coordinate = None
    for c in coordinates:
        d = distance(coordinate, c)
        if 0 < d < lowest_distance:
            closest_coordinate = c
            lowest_distance = d
    return lowest_distance, closest_coordinate


distances = []
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        d = distance(coordinates[i], coordinates[j])
        heapq.heappush(distances, (d, coordinates[i], coordinates[j]))


class UnionFind:
    def __init__(self, elements):
        self.parent = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}
        self.size = {element: 1 for element in elements}

    def find(self, element):
        if self.parent[element] != element:  # Fixed
            self.parent[element] = self.find(self.parent[element])  # Path compression
        return self.parent[element]

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            self.size.pop(root2)
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
            self.size.pop(root1)
        else:
            self.rank[root1] += 1
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
            self.size.pop(root2)
        return True


uf = UnionFind(coordinates)
count = 0
while distances:
    if count == len(coordinates):
        break
    _d, coordinate, other_coordinate = heapq.heappop(distances)
    uf.union(coordinate, other_coordinate)
    count += 1

circuit_sizes = sorted(uf.size.values(), reverse=True)
result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
print("part 1", result)


last_coord1, last_coord2 = None, None
while len(uf.size) > 1:
    _d, coordinate, other_coordinate = heapq.heappop(distances)
    if uf.union(coordinate, other_coordinate):
        last_coord1, last_coord2 = coordinate, other_coordinate

print("part 2:", last_coord1[0] * last_coord2[0])
