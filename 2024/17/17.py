with open("17.txt") as f:
    lines = f.readlines()


register = {
    "A": int(lines[0].split(":")[1].strip()),
    "B": int(lines[1].split(":")[1].strip()),
    "C": int(lines[2].split(":")[1].strip()),
}

programs = lines[4].split(":")[1].strip().split(",")
programs = list(map(int, programs))
pointer = 0
res = []


def combo_operand(x):
    if 0 <= x <= 3:
        return x
    match x:
        case 4:
            return register["A"]
        case 5:
            return register["B"]
        case 6:
            return register["C"]


def adv(operand):
    register["A"] //= 2 ** combo_operand(operand)


def bxl(operand):
    register["B"] = register["B"] ^ operand


def bst(operand):
    register["B"] = combo_operand(operand) % 8


def jnz(operand):
    global pointer
    if register["A"] != 0:
        pointer = operand
    else:
        pointer += 2


def bxc(operand):
    register["B"] = register["B"] ^ register["C"]


def out(operand):
    result = combo_operand(operand) % 8
    res.append(str(result))


def bdv(operand):
    register["B"] = register["A"] // 2 ** combo_operand(operand)


def cdv(operand):
    register["C"] = register["A"] // 2 ** combo_operand(operand)


instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def run_program(opcode, operand):
    instruction_map[opcode](operand)


def run_sequence():
    global pointer
    while pointer < len(programs):
        opcode = programs[pointer]
        operand = programs[pointer + 1]

        # Run the instruction
        if opcode == 3:  # Special case for `jnz`
            jnz(operand)
            continue
        else:
            run_program(programs[pointer], programs[pointer + 1])

        # Move to the next instruction
        pointer += 2
    print(",".join(res))
    return res


# Part 1
run_sequence()

# Part 2
out = []
backup_value = 8**15
power = 14
matched = programs[-1:]

while out != programs:
    backup_value += 8**power
    res = []
    pointer = 0
    register["A"] = backup_value
    register["B"] = 0
    register["C"] = 0
    out = list(map(int, run_sequence()))
    if out[-len(matched) :] == matched:
        power = max(0, power - 1)
        matched = programs[-(len(matched) + 1) :]
print(backup_value)
