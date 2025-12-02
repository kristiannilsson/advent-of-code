from collections import Counter


with open("11.txt") as f:
    stones = Counter(map(int, f.readline().split()))


def split_stones(stones):
    res = Counter()
    for value, count in stones.items():
        if value == 0:
            res[1] += count
        else:
            digits = len(str(value))
            if digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                res[value // divisor] += count
                res[value % divisor] += count
            else:
                res[value * 2024] += count
    return res


# Iteratively split stones for 75 iterations.
for _ in range(75):
    # print(len(stones), stones)
    stones = split_stones(stones)


# Print the final count of stones.
total = 0
for count in stones.values():
    total += count
print(total)
