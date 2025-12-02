import math


with open("1.txt") as f:
    lines = f.readlines()

n = 50
count = 0
for line in lines:
    direction = line[0]
    amount = line[1:]

    if direction == "L":
        n -= int(amount)
    else:
        n += int(amount)
    n = n % 100
    if n == 0:
        count += 1

#######

n = 50
count = 0
for line in lines:
    direction = line[0]
    amount = int(line[1:])
    rotation = 0

    if direction == "L":
        if n > 0:
            step = n
        else:
            step = 100

        while step <= amount:
            count += 1
            step += 100
        n = (n - amount) % 100
    else:
        step = 100 - n
        while step <= amount:
            count += 1
            step += 100
        n = (n + amount) % 100

    print(n, count, line)
print(count)
