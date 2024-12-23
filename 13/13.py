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


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def solve_diophantine(a, b, c):
    """
    Solves the linear Diophantine equation ax + by = c.
    Returns a tuple (x, y, g), where (x, y) is a particular solution,
    and g is the gcd(a, b).
    If no solution exists, returns None.
    """
    g, x0, y0 = extended_gcd(a, b)

    # Check if the equation has integer solutions
    if c % g != 0:
        return None  # No solution exists

    # Scale the particular solution to the desired c
    x0 *= c // g
    y0 *= c // g

    bounds = (math.ceil(-x0 * g / b), math.ceil(y0 * g / a))

    return lambda t: (x0 + (b // g) * t, y0 - (a // g) * t), bounds


def generate_y_equation(a, b):
    return lambda x, y: (a * x + b * y)


tokens = 0
for machine in machines:
    print(machine)
    res = solve_diophantine(machine["A"]["X"], machine["B"]["X"], machine["Prize"]["X"])
    if res is None:
        continue
    x_equation, bound = res
    lowest_sum = float("inf")
    y_equation = generate_y_equation(machine["A"]["Y"], machine["B"]["Y"])
    print(x_equation(bound[1]))
    """ for t in range(*bound):
        print(t)
        x, y = x_equation(t)
        if 3 * x + y < lowest_sum and y_equation(x, y) == machine["Prize"]["Y"]:
            lowest_sum = 3 * x + y
    tokens += 0 if lowest_sum == float("inf") else lowest_sum """
print(tokens)
