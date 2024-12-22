with open("9.txt") as f:
    input = f.readline()
res = []
for i, disk_reading in enumerate(input):
    if i % 2 == 0:
        res.extend([i // 2] * int(disk_reading))
    else:
        res.extend(["."] * int(disk_reading))

first_pointer = 0
second_pointer = len(res) - 1


while first_pointer < second_pointer:

    while first_pointer < len(res) and res[first_pointer] != ".":
        first_pointer += 1
    if first_pointer >= second_pointer:
        break
    res[first_pointer] = res[second_pointer]
    res[second_pointer] = "."
    while second_pointer > 0 and res[second_pointer] == ".":
        second_pointer -= 1

pointer = 0
checksum = 0
while pointer < len(res) and res[pointer] != ".":
    checksum += pointer * res[pointer]
    pointer += 1
print(checksum)
