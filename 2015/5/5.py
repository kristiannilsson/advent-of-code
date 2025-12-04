with open("5.txt") as f:
    strings = f.readlines()


def is_nice(string):
    vowels = set(["a", "e", "i", "o", "u"])
    forbidden = set(["ab", "cd", "pq", "xy"])

    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                break
    if vowel_count < 3:
        return False

    has_repating_characters = False
    for i in range(len(string) - 1):
        window = string[i : i + 2]
        if window in forbidden:
            return False
        if string[i] == string[i + 1]:
            has_repating_characters = True

    return has_repating_characters


count = 0
for string in strings:
    if is_nice(string):
        count += 1

print(count)
