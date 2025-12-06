import math


with open("6.txt") as f:
    lines = f.read().splitlines()


operations = lines.pop()

res = 0
current_res = []


for i in range(len(operations) - 1, -1, -1):
    current_digit = ""
    for j in range(len(lines)):
        if lines[j][i] == " ":
            continue
        current_digit += lines[j][i]
    if current_digit:
        current_res.append(int(current_digit))
    print(current_res)
    if operations[i] != " ":
        if operations[i] == "*":
            print(math.prod(current_res))
            res += math.prod(current_res)
        else:
            print(sum(current_res))
            res += sum(current_res)
        current_res = []
print(res)
