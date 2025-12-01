with open("3.txt") as f:
    s = f.read()

i = 0

seq_start = "mul("
seq_enable = "do()"
seq_disable = "don't()"

sequence_enabled = True
allowed_characters = "0123456789,)"

multipliers = []
while i < len(s):
    if s[i : i + 4] == seq_enable:
        i += 4
        sequence_enabled = True
    if s[i : i + 7] == seq_disable:
        i += 7
        sequence_enabled = False
    if s[i : i + 4] == seq_start:

        i += 4
        j = i
        while s[j] in allowed_characters and sequence_enabled:
            if s[j] == ")":
                multipliers.append(s[i:j])
                break
            j += 1
    i += 1

total_sum = 0
for multiplier in multipliers:
    factors = multiplier.split(",")
    if len(factors) != 2:
        continue
    total_sum += int(factors[0]) * int(factors[1])
print(total_sum)
