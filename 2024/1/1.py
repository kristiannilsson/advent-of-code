with open("1.txt") as f:
    lines = f.readlines()
num1 = []
num2 = []
for line in lines:
    numbers = line.split("   ")
    num1.append(int(numbers[0]))
    num2.append(int(numbers[1].replace("\n", "")))

num1.sort()
num2.sort()

res = 0
for i in range(len(num1)):
    res += abs(num1[i] - num2[i])
print(res)

counter = {}

for num in num2:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

similarity = 0

for num in num1:
    similarity += num * counter.get(num, 0)
print(similarity)