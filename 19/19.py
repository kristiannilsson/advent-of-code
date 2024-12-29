with open("19.txt") as f:
    lines = []
    for i, line in enumerate(f):
        if line == "\n":
            split_index = i
        lines.append(line.strip())
patterns = " ".join(lines[:split_index]).split(", ")
designs = lines[split_index + 1 :]

possible_designs = 0
possible_unique_designs = 0
for design in designs:
    n = len(design)
    can_form_substring = [0] * (n + 1)
    can_form_substring[0] = 1

    for i in range(1, n + 1):
        for pattern in patterns:
            starting_index = i - len(pattern)
            if starting_index < 0:
                continue
            if (
                can_form_substring[starting_index]
                and design[starting_index:i] == pattern
            ):
                can_form_substring[i] += can_form_substring[starting_index]
    possible_unique_designs += min(1, can_form_substring[n])
    possible_designs += can_form_substring[n]
print(possible_unique_designs, possible_designs)
