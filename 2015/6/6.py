with open("6.txt") as f:
    lines = f.read().splitlines()

instructions = []
starts = []
ends = []

for line in lines:
    parts = line.split()
    instruction = ""
    valid_instruction = set(["turn", "toggle", "on", "off"])
    start = None
    end = None
    for part in parts:
        if part == "through":
            continue
        if part in valid_instruction:
            instruction += part
            continue
        if start is None:
            raw = part.split(",")
            start = (int(raw[0]), int(raw[1]))
            continue
        raw = part.split(",")
        end = (int(raw[0]), int(raw[1]))
    instructions.append(instruction)
    starts.append(start)
    ends.append(end)


# Strategy functions for Part 1
def part1_strategy(instruction, current_value):
    match instruction:
        case "turnon":
            return 1
        case "turnoff":
            return 0
        case "toggle":
            return 1 - current_value


# Strategy functions for Part 2
def part2_strategy(instruction, current_value):
    match instruction:
        case "turnon":
            return current_value + 1
        case "turnoff":
            return max(current_value - 1, 0)
        case "toggle":
            return current_value + 2


def solve(strategy):
    GRID_LENGTH = 1000
    grid = [[0] * GRID_LENGTH for _ in range(GRID_LENGTH)]

    def perform_instruction(instruction, start, end):
        x, y = start
        end_x, end_y = end
        for i in range(y, end_y + 1):
            for j in range(x, end_x + 1):
                grid[i][j] = strategy(instruction, grid[i][j])

    for i in range(len(instructions)):
        perform_instruction(instructions[i], starts[i], ends[i])

    return sum(sum(row) for row in grid)


print("Part 1:", solve(part1_strategy))
print("Part 2:", solve(part2_strategy))
