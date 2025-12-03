with open("3.txt") as f:
    lines = f.read().splitlines()


def get_joltage(line, joltage_length):
    highest_digits = [0] * joltage_length
    for i in range(len(line)):
        digit_start_index = max(0, joltage_length - len(line) + i)
        has_replaced_digit = False
        for j in range(digit_start_index, joltage_length):
            if has_replaced_digit:
                highest_digits[j] = 0
            elif highest_digits[j] < int(line[i]):
                highest_digits[j] = int(line[i])
                has_replaced_digit = True
    return get_joltage_sum(highest_digits)


def get_joltage_sum(joltage):
    res = 0
    for i in range(len(joltage)):
        res += joltage[i] * 10 ** (len(joltage) - i - 1)
    return res


part1 = 0
part2 = 0
for line in lines:
    part1 += get_joltage(line, 2)
    part2 += get_joltage(line, 12)
print(part1)
print(part2)
