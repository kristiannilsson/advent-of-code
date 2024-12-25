import math

machines = []
with open("13.txt") as f:
    block = {}
    for line in f:
        line = line.strip()
        if line.startswith("Button A:"):
            parts = line.replace("Button A:", "").strip().split(", ")
            block["A"] = {
                "X": int(parts[0].split("+")[1]),
                "Y": int(parts[1].split("+")[1]),
            }
        elif line.startswith("Button B:"):
            parts = line.replace("Button B:", "").strip().split(", ")
            block["B"] = {
                "X": int(parts[0].split("+")[1]),
                "Y": int(parts[1].split("+")[1]),
            }
        elif line.startswith("Prize:"):
            parts = line.replace("Prize:", "").strip().split(", ")
            block["Prize"] = {
                "X": int(parts[0].split("=")[1]) + 10000000000000,
                "Y": int(parts[1].split("=")[1]) + 10000000000000,
            }
            # Save the block and reset for the next one
            machines.append(block)
            block = {}


def find_intersection(a1, b1, c1, a2, b2, c2):
    determinant = a2 * b1 - a1 * b2
    if determinant == 0:
        print("det 0")
        if c2 / c1 == b2 / b1:
            print("Infinite")
        return None
    y = (c1 * a2 - c2 * a1) / determinant
    x = (c1 - b1 * y) / a1
    if not x.is_integer() or not y.is_integer():
        return None
    return (x, y)

tokens = 0
for machine in machines:
    intersection = find_intersection(
        machine["A"]["X"],
        machine["B"]["X"],
        machine["Prize"]["X"],
        machine["A"]["Y"],
        machine["B"]["Y"],
        machine["Prize"]["Y"],
    )
    if not intersection:
        continue
    x, y = intersection
    tokens += 3*x + y
print(tokens)