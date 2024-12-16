from itertools import product


with open("4.txt") as f:
    lines = f.read().split("\n")


search_directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
word = "XMAS"
word_count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        for direction in search_directions:
            row, col = i, j
            is_word = True
            for letter in word:
                if not (0 <= row < len(lines)) or not (0 <= col < len(lines[i])):
                    is_word = False
                    break
                c = lines[row][col]
                if c != letter:
                    is_word = False
                    break
                row += direction[0]
                col += direction[1]
            if is_word:
                word_count += 1


print(word_count)
