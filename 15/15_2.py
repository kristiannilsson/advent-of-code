from collections import defaultdict

def load_input():
    with open("15.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    split_index = lines.index("")
    grid = []
    new_grid_map = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
    for line in lines[:split_index]:
        row = []
        for c in line:
            row += new_grid_map[c]
        grid.append(row)
    instructions = "".join(lines[split_index + 1 :])
    return grid, instructions


def find_starting_position(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "@":
                return j, i
    return None


directions_map = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}
other_box_map = {"[": ("]", 1), "]": ("[", -1)}

grid, instructions = load_input()
x, y = find_starting_position(grid)

def get_boxes_to_push_vertical(grid, x, y, dy):

    stack = [(x, y)]
    res = defaultdict(dict)
    while stack:
        x, y = stack.pop()
        if grid[y+dy][x] == "#":
            res = {}
            break
        if grid[y+dy][x] in ("[", "]"):
            char = grid[y+dy][x]
            other_char, dx = other_box_map[char]
            stack.extend([(x, y+dy), (x+dx, y+dy)])
            res[y+2*dy][x] = char
            res[y+2*dy][x+dx] = other_char
            if not res.get(y+dy, {}).get(x):
                res[y+dy][x] = "."
            if not res.get(y+dy, {}).get(x+dx):
                res[y+dy][x+dx] = "."

    return res

def get_boxes_to_push_horizontal(grid, x, y, dx):
    boxes = 0
    res = defaultdict(dict)
    while grid[y][x+(boxes+1)*dx] in ("[", "]"):
        boxes += 1
        res[y][x+(boxes+1)*dx] = grid[y][x+boxes*dx]
    if grid[y][x+(boxes+1)*dx] == "#":
        res = {}
    return res

for instruction in instructions:
    dx, dy = directions_map[instruction]
    new_x, new_y = x + dx, y + dy
    coordinates = {}
    if grid[new_y][new_x] in ("[", "]"):
        if dx != 0:
            coordinates = get_boxes_to_push_horizontal(grid, x, y, dx)
        if dy != 0:
            coordinates = get_boxes_to_push_vertical(grid, x, y, dy)
        if not coordinates:
            new_x, new_y = x, y
    if grid[new_y][new_x] == "#":
        new_x, new_y = x, y

 
    for row, value in coordinates.items():
        for col, char in value.items():
            grid[row][col] = char

    grid[y][x] = "."
    grid[new_y][new_x] = "@"
    x, y = new_x, new_y





def get_rock_sum(grid):
    sum = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "[":
                sum += i * 100 + j
    return sum


print(get_rock_sum(grid))
