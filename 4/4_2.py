with open("4.txt") as f:
    lines = f.read().splitlines()

word_count = 0


def is_valid_word(i, j, lines):
    if lines[i][j] != "A":
        return False

    top_left = lines[i - 1][j - 1]
    top_right = lines[i - 1][j + 1]
    bottom_left = lines[i + 1][j - 1]
    bottom_right = lines[i + 1][j + 1]
    diag1 = {top_left, bottom_right}  # should be {'M', 'S'}
    diag2 = {top_right, bottom_left}  # should be {'M', 'S'}
    return diag1 == {"M", "S"} and diag2 == {"M", "S"}


res = []
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if is_valid_word(i, j, lines):
            word_count += 1
print(word_count)
