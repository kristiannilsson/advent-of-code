with open("5.txt") as f:
    lines = f.read().splitlines()


def merge_ranges(ranges):
    merged = []
    for lower, upper in ranges:
        if not merged:
            merged.append((lower, upper))
            continue
        current_lower, current_upper = merged[-1]
        if current_upper < lower - 1:
            merged.append((lower, upper))
            continue
        merged[-1] = (merged[-1][0], max(merged[-1][1], upper))
    return merged


ranges = []
ids = []
is_parsing_ids = False

for line in lines:
    if is_parsing_ids:
        ids.append(int(line))
        continue
    if line == "":
        is_parsing_ids = True
        continue
    lower, upper = line.split("-")
    ranges.append((int(lower), int(upper)))

ranges.sort()
merged_ranges = merge_ranges(ranges)

count = 0
for id in ids:
    for lower, upper in merged_ranges:
        if lower <= id <= upper:
            count += 1
            break

print(f"Part 1: {count}")

count = 0
for lower, upper in merged_ranges:
    count += upper - lower + 1
print(f"Part 2: {count}")
