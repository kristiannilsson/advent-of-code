with open("2.txt") as f:
    lines = f.readlines()


reports = []
for line in lines:
    line = line.split()
    reports.append([int(c) for c in line])


def outside_safe_change(first, second):
    diff = second - first
    # "Outside safe" if the absolute difference is not between 1 and 3 (inclusive).
    return not (1 <= abs(diff) <= 3)


def safe_report(level):
    direction = level[1] - level[0]
    if direction == 0:
        return (False, 1)
    for i in range(1, len(level)):
        difference = level[i] - level[i - 1]
        if difference / direction < 0 or outside_safe_change(level[i - 1], level[i]):
            return (False, i)
    return (True, -1)


safe_reports = 0
for level in reports:
    if safe_report(level)[0]:
        safe_reports += 1

safe_reports_with_removal = 0
for level in reports:
    safe_without_removal, i = safe_report(level)
    if safe_without_removal:
        # Already safe
        safe_reports_with_removal += 1
    else:
        # Try removing one element around the problematic index to see if that helps
        candidates = [
            level[:i] + level[i + 1 :],  # remove the problematic element
            level[: i - 1]
            + level[i:],  # remove the element before the problematic index
            level[1:],  # remove the first element, as tried in the original code
        ]

        if any(safe_report(candidate)[0] for candidate in candidates):
            safe_reports_with_removal += 1
