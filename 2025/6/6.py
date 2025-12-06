with open("6.txt") as f:
    lines = f.read().splitlines()


last_row = lines.pop().split(" ")
operations = []

for operation in last_row:
    if operation == "":
        continue
    operations.append(operation)

res = []
for operation in operations:
    if operation == "+":
        res.append(0)
    else:
        res.append(1)

for line in lines:
    operation_index = 0
    line_index = 0
    nums = line.split(" ")
    while operation_index < len(operations):
        if nums[line_index] == "":
            line_index += 1
            continue
        num = int(nums[line_index])
        if operations[operation_index] == "+":
            res[operation_index] += num
        else:
            res[operation_index] *= num
        line_index += 1
        operation_index += 1

print(sum(res))
