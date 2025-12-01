def get_robots():
    with open("14.txt") as f:
        robots = []
        for line in f:
            robot = {}
            position, velocity = line.split()

            position = position.split("=")[1]
            position = tuple(map(int, position.split(",")))

            velocity = velocity.split("=")[1]
            velocity = tuple(map(int, velocity.split(",")))

            robot["position"] = position
            robot["velocity"] = velocity

            robots.append(robot)
    return robots

bathroom_width = 101
bathroom_height = 103
seconds = 100

def move_robots(robots, iterations):
    new_positions = []

    for robot in robots:
        dx, dy = robot["velocity"]
        x, y = robot["position"]

        x += iterations * dx
        y += iterations * dy

        x %= bathroom_width
        y %= bathroom_height

        robot["position"] = (x,y)

def get_safety_score(robots):
    quadrants = {"1": 0, "2": 0, "3": 0, "4": 0}
    mid_x = bathroom_width // 2
    mid_y = bathroom_height // 2

    for robot in robots:
        x, y = robot["position"]
        if x < mid_x and y < mid_y:
            quadrants["1"] += 1
        elif x > mid_x and y < mid_y:
            quadrants["2"] += 1
        elif x < mid_x and y > mid_y:
            quadrants["3"] += 1
        elif x > mid_x and y > mid_y:
            quadrants["4"] += 1

    product = 1
    for value in quadrants.values():
        product *= value
    return product

robots = get_robots()
positions = move_robots(robots, seconds)
safety_score = get_safety_score(robots)
print(safety_score)

# Part two
def draw_robots(robots, width, height):
    # Create an empty grid
    grid = [["." for _ in range(width)] for _ in range(height)]
    
    # Place robots on the grid
    for robot in robots:
        x, y = robot["position"]
        grid[y][x] = "R"
    
    # Convert the grid to a string representation
    grid_str = "\n".join("".join(row) for row in grid)
    print(grid_str)

robots = get_robots()
minimal_safety = (float("inf"), 0)
for i in range(101*103):
    for robot in robots:
        dx, dy = robot["velocity"]
        x, y = robot["position"]

        x += dx
        y += dy

        x %= bathroom_width
        y %= bathroom_height

        robot["position"] = (x, y)
    if i == 7671:
        draw_robots(robots, bathroom_width, bathroom_height) # This was done after knowing the answer
    safety, index = minimal_safety
    current_safety = get_safety_score(robots)
    if current_safety < safety:
        minimal_safety = (current_safety, i+1)
print(minimal_safety)