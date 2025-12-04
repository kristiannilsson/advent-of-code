with open("2.txt") as f:
    lines = f.read().splitlines()
dimensions = []

for line in lines:
    string_dimensions = line.split("x")
    print(string_dimensions)
    dimension = []
    for string_dimension in string_dimensions:
        dimension.append(int(string_dimension))
    dimension.sort()
    dimensions.append(dimension)

paper = 0
ribbon = 0
for a, b, c in dimensions:
    smallest_side = a * b
    smallest_perimeter = 2 * a + 2 * b

    paper += 2 * (a * b + b * c + c * a)
    paper += smallest_side

    ribbon += smallest_perimeter + a * b * c

print(paper)
print(ribbon)
