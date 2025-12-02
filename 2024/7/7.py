import math


with open("7.txt") as f:
    lines = [line.split(":") for line in f]

equations = [(int(key), list(map(int, values.split()))) for key, values in lines]


def possibly_true(total, values):
    if total % 1 != 0:
        return False
    if len(values) == 1:
        return values[0] == total
    last_value = values[-1]
    digits = int(math.log10(last_value) + 1)
    return (
        possibly_true(total / last_value, values[:-1])
        or possibly_true(total - last_value, values[:-1])
        or possibly_true((total - last_value) / 10**digits, values[:-1])
    )


test_sum = 0
for total, values in equations:
    if possibly_true(total, values):
        test_sum += total

print(test_sum)
