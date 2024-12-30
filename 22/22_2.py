from collections import defaultdict
from time import time

start = time()

with open("22.txt") as f:
    secrets = map(int, f.readlines())


def generate_secret(secret):
    num = 64 * secret
    secret ^= num
    secret %= 16777216

    num = secret // 32
    secret ^= num
    secret %= 16777216

    num = secret * 2048
    secret ^= num
    secret %= 16777216
    return secret


global_sums = defaultdict(int)

for secret in secrets:
    d = []
    pattern = {}
    price = secret % 10
    for j in range(2001):
        # Generate differences in d.
        secret = generate_secret(secret)
        d.append(secret % 10 - price)
        price = secret % 10

        # Add sequence to the dictionary.
        if j < 3:
            continue
        sequence = (d[j - 3], d[j - 2], d[j - 1], d[j])
        if sequence in pattern:
            continue
        pattern[sequence] = price
    for sequence, earliest_price in pattern.items():
        global_sums[sequence] += earliest_price

best_sequence, best_sum = None, 0
for seq, total in global_sums.items():
    if total > best_sum:
        best_sum = total
        best_sequence = seq
print(best_sequence, best_sum)
print(time() - start)
