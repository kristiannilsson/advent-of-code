from time import perf_counter
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

time_start = perf_counter()
with open("10.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

instructions = []
for line in lines:
    row = {}
    row["objective"] = [1] * len(line[1:-1])
    row["bounds"] = [(0, None)] * len(line[1:-1])
    row["joltage"] = list(map(int, line[-1][1:-1].split(",")))
    row["buttons"] = [[0] * len(line[1:-1]) for _ in range(len(row["joltage"]))]
    for i, instruction in enumerate(line[1:-1]):
        for button in instruction[1:-1].split(","):
            row["buttons"][int(button)][i] = 1
    instructions.append(row)

s = 0
for instruction in instructions:
    # Convert to numpy arrays
    c = np.array(instruction["objective"])
    A_eq = np.array(instruction["buttons"])
    b_eq = np.array(instruction["joltage"])

    # Create constraints (equality: lb = ub)
    constraints = LinearConstraint(A_eq, b_eq, b_eq)

    # Create bounds
    bounds = Bounds(0, np.inf)

    # Set all variables to integers
    integrality = np.ones(len(c))

    # Solve with milp
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    if result.success:
        s += sum(result.x)
    else:
        print(f"Warning: Optimization failed - {result.message}")

print(s)

time_end = perf_counter()
time_duration = time_end - time_start
print(f"Took {time_duration:.3f} seconds")
