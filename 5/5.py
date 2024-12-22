from collections import defaultdict

rules = defaultdict(set)
updates = []

with open("5.txt") as f:
    lines = f.readlines()

split_index = lines.index("\n")

# All rules
for line in lines[:split_index]:
    key, value = line.split("|")
    key, value = int(key), int(value)
    rules[key].add(value)

# All updates
for line in lines[split_index + 1 :]:
    nums = map(int, line.split(","))
    updates.append(list(nums))


def sort_input(page_sequence):
    current_pages = set(page_sequence)
    pages_graph = defaultdict(set)
    number_of_references = defaultdict(int)

    for page in page_sequence:
        for ref in rules[page]:
            if ref in current_pages:
                pages_graph[page].add(ref)
                number_of_references[ref] += 1

    # Create the first pages without references.
    queue = []
    for page, ref in pages_graph.items():
        if number_of_references[page] == 0:
            queue.append((page, ref))

    sorted_order = []
    current_index = 0
    is_sorted = True
    # Create the sorted order
    while queue:
        page, ref = queue.pop()
        if page_sequence[current_index] != page:
            is_sorted = False
        current_index += 1
        sorted_order.append(page)

        for ref in ref:
            number_of_references[ref] -= 1
            if number_of_references[ref] == 0:
                queue.append((ref, pages_graph[ref]))
    return (is_sorted, sorted_order[len(sorted_order) // 2])


total_sorted = 0
total_unsorted = 0
for update in updates:
    sorted, total = sort_input(update)
    if sorted:
        total_sorted += total
    else:
        total_unsorted += total
print(total_sorted, total_unsorted)
