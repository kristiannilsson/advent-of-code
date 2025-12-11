with open("10.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]

instructions = []
for line in lines:
    row = {}
    row["res"] = [1 if button == "#" else 0 for button in line[0][1:-1]]
    row["joltage"] = line[-1]
    row["buttons"] = []
    for instruction in line[1:-1]:
        buttons = map(int, instruction[1:-1].split(","))
        row["buttons"].append(tuple(buttons))
    instructions.append(row)

def press_button(buttons, current_config):
    for indicator in buttons:
        current_config[indicator] = (current_config[indicator] + 1) % 2

def unpress_button(buttons, current_config):
    for indicator in buttons:
        current_config[indicator] = (current_config[indicator] - 1) % 2


def calculate_min_button_presses(row):
    print(row)
    current_config = [0] * len(row["res"])
    res = [float("inf")]
    active_buttons = [0]
    buttons_pressed = []
    def backtrack(index):
        if active_buttons[0] > res[0]:
            return
        if current_config == row["res"]:
            res[0] = active_buttons[0]
        if index >= len(row["buttons"]):
            return
        backtrack(index + 1)
        press_button(row["buttons"][index], current_config)
        buttons_pressed.append(index)
        active_buttons[0] += 1
        backtrack(index + 1)
        unpress_button(row["buttons"][index], current_config)
        active_buttons[0] -= 1
        buttons_pressed.pop()

    backtrack(0)

    return res[0]

s = 0
for instruction in instructions:
    s += calculate_min_button_presses(instruction)

print(s)