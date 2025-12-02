import math


with open("2.txt") as f:
    line = f.readline()

raw_intervals = line.split(",")

intervals = []

for interval in raw_intervals:
    lower, upper = interval.split("-")
    intervals.append((int(lower), int(upper)))

intervals.sort()

max_value = str(intervals[-1][1])

max_id = int(max_value[: len(max_value) // 2])

res = 0
for i in range(max_id):
    id = int(str(i) * 2)
    for lower, upper in intervals:
        if lower <= id <= upper:
            res += id
            break
print(res)

### 2
invalid_ids = set()
for i in range(max_id):
    id = str(i)
    repeats = 2
    while len(id) * repeats <= len(max_value):
        invalid_id = int(id * repeats)
        for lower, upper in intervals:
            if lower <= invalid_id <= upper:
                invalid_ids.add(invalid_id)
                break
        repeats += 1
print(sum(invalid_ids))
