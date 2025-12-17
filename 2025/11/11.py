with open("11.txt") as f:
    lines = f.read().splitlines()

paths = {}
for line in lines:
    parts = line.split(":")
    paths[parts[0]] = parts[1].strip().split(" ")


def unique_paths(start, end):
    cache = {}

    def dfs(paths_to_traverse, end_node):
        count = 0
        for path in paths_to_traverse:
            if path == end_node:
                count += 1
                continue
            if path not in paths:
                continue
            if path in cache:
                count += cache[path]
            else:
                res = dfs(paths[path], end_node)
                count += res
                cache[path] = res
        return count

    return dfs(paths[start], end)


print("part 1", unique_paths("you", "out"))

a = unique_paths("svr", "dac") * unique_paths("dac", "fft") * unique_paths("fft", "out")
b = unique_paths("svr", "fft") * unique_paths("fft", "dac") * unique_paths("dac", "out")

print("part 2", a + b)
