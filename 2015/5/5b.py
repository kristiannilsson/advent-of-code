with open("5.txt") as f:
    strings = f.read().splitlines()


def is_nice(string):
    pairs = {}
    has_two_pairs = False

    for i in range(len(string) - 1):

        if (string[i], string[i + 1]) in pairs and i - pairs[
            (string[i], string[i + 1])
        ] > 1:
            has_two_pairs = True
            break
        pairs[(string[i], string[i + 1])] = i
    if not has_two_pairs:
        return False

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


count = 0
for string in strings:
    if is_nice(string):
        count += 1

print(count)
