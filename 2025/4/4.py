paper = []

with open("4.txt") as f:
    lines = f.read().splitlines()

paper = [list(line) for line in lines]


def square_has_paper_roll(x, y, paper):
    if not (0 <= y < len(paper) and 0 <= x < len(paper[0])):
        return False
    return paper[y][x] == "@"


def is_not_blocked(x, y, paper):
    adjacent_paper_rolls = 0
    directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    for direction in directions:
        dy, dx = direction
        if square_has_paper_roll(x + dx, y + dy, paper):
            adjacent_paper_rolls += 1
    return adjacent_paper_rolls < 4


def remove_paper_rolls(paper):
    count = 0
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] != "@":
                continue
            if is_not_blocked(j, i, paper):
                paper[i][j] = "."
                count += 1
    return count


count = remove_paper_rolls(paper)
print("part 1", count)

total = count
while True:
    removed_paper_rolls = remove_paper_rolls(paper)
    if removed_paper_rolls == 0:
        break
    total += removed_paper_rolls

print("part 2", total)
