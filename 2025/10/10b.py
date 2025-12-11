from time import perf_counter


time_start = perf_counter()
with open("10.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

instructions = []
for line in lines:
    row = {}
    row["res"] = [1 if button == "#" else 0 for button in line[0][1:-1]]
    row["joltage"] = list(map(int, line[-1][1:-1].split(",")))
    row["buttons"] = []
    for instruction in line[1:-1]:
        buttons = map(int, instruction[1:-1].split(","))
        row["buttons"].append(tuple(buttons))
    instructions.append(row)

def press_button(buttons, current_config, buttons_pressed):
    for indicator in buttons:
        current_config[indicator] = (current_config[indicator] + 1)
    buttons_pressed[0] += 1

def unpress_button(buttons, current_config, buttons_pressed):
    for indicator in buttons:
        current_config[indicator] = (current_config[indicator] - 1)
    buttons_pressed[0] -= 1


def calculate_min_button_presses(row):
    current_config = [0] * len(row["joltage"])
    res = [float("inf")]
    buttons_pressed = [0]
    def backtrack(start):
        if buttons_pressed[0] >= res[0]:
            return
        if current_config == row["joltage"]:
            res[0] = buttons_pressed[0]
        for i in range(len(current_config)):
            if current_config[i] > row["joltage"][i]:
                return
        for i in range(start, len(row["buttons"])):
            press_button(row["buttons"][i], current_config, buttons_pressed)
            #print(row["buttons"][i])
            backtrack(i)
            unpress_button(row["buttons"][i], current_config, buttons_pressed)

    backtrack(0)

    return res[0]

s = 0
for i, instruction in enumerate(instructions):
    print(i)
    s += calculate_min_button_presses(instruction)
print(s)

time_end = perf_counter()
# calculate the duration
time_duration = time_end - time_start
# report the duration
print(f'Took {time_duration:.3f} seconds')