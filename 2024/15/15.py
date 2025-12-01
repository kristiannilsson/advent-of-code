with open("15.txt") as f:
    lines = [line.strip() for line in f.readlines()]

for i, line in enumerate(lines):
    if line == "":
        split_index = i

grid = lines[:split_index]
instructions = ''.join(lines[split_index + 1:])
grid = [list(line) for line in grid]
def find_starting_position(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "@":
                return j, i
    return None

directions_map = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}
x, y = find_starting_position(grid)
for instruction in instructions:
    dx, dy = directions_map[instruction]
    new_x, new_y = x+dx, y+dy
    rocks = 0
    while grid[new_y+rocks*dy][new_x+rocks*dx] == "O":
        rocks += 1
    if grid[new_y+rocks*dy][new_x + rocks*dx] == "#":
        new_x, new_y = x, y
    if rocks > 0 and grid[new_y+rocks*dy][new_x+rocks*dx] == ".":
        grid[new_y+rocks*dy][new_x+rocks*dx] = "O"
    
    
    grid[y][x] = "."
    grid[new_y][new_x] = "@"
    x, y = new_x, new_y

def get_rock_sum(grid):
    sum = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "O":
                sum += i*100 + j
    return sum

for line in grid:
    print(line)
print(get_rock_sum(grid))