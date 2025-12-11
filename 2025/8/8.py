import math


class CircuitNode:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return str(self.val)

    def distance(self, other):
        x1, y1, z1 = self.val
        x2, y2, z2 = other.val
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


with open("8.txt") as f:
    lines = f.read().splitlines()

coordinates = []

for line in lines:
    raw_coordinates = map(int, line.split(","))
    coordinates.append(CircuitNode(tuple(raw_coordinates)))
coordinates.sort()


def find_closest_node(node):
    res = None
    lowest_distance = float("inf")
    for other_node in coordinates:
        if other_node == node:
            continue
        distance = node.distance(other_node)
        if distance < lowest_distance:
            lowest_distance = distance
            res = other_node
        lowest_distance = min(lowest_distance, node.distance(other_node))
    return res


circuits = []
for node in coordinates:
    other_node = find_closest_node(node)
    found_circuit = False
    for circuit in circuits:
        if other_node in circuit:
            circuit.add(node)
            found_circuit = True
            break
    if not found_circuit:
        circuits.append(set([node, other_node]))

circuits.sort(key=len, reverse=True)
for circuit in circuits[:3]:
    print(len(circuit))
