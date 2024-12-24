import collections

def solve_racetrack(filename="20.txt"):
    # --- Read and prepare grid ---
    with open(filename) as f:
        grid = [line.rstrip("\n") for line in f]

    rows = len(grid)
    cols = len(grid[0])
    
    # --- Find start and end points ---
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)
    if not start or not end:
        print("Start or End not found.")
        return

    # --- BFS state and distance tracking ---
    distances = [[[float('inf')] * 2 for _ in range(cols)] for _ in range(rows)]
    sr, sc = start
    distances[sr][sc][0] = 0  # Starting with no cheat
    queue = collections.deque([(sr, sc, 0)])  # (row, col, used_cheat)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cheats = []  # List of (saving, cheat_start, cheat_end)

    # --- BFS Traversal ---
    while queue:
        r, c, used_cheat = queue.popleft()
        current_dist = distances[r][c][used_cheat]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = grid[nr][nc]

                # --- Normal movement ---
                if cell != "#":
                    if distances[nr][nc][used_cheat] > current_dist + 1:
                        distances[nr][nc][used_cheat] = current_dist + 1
                        queue.append((nr, nc, used_cheat))
                
                # --- Cheat movement ---
                elif used_cheat == 0:
                    # Try passing through exactly 2 walls
                    nnr, nnc = nr + dr, nc + dc
                    if 0 <= nnr < rows and 0 <= nnc < cols and grid[nnr][nnc] != "#":
                        # Land back on track
                        if distances[nnr][nnc][1] > current_dist + 3:  # 2 for walls + 1 for landing
                            distances[nnr][nnc][1] = current_dist + 3
                            queue.append((nnr, nnc, 1))
                            saving = distances[sr][sc][0] - distances[nnr][nnc][1]
                            cheats.append((saving, (r, c), (nnr, nnc)))

    # --- Analyze Cheats ---
    saving_counts = collections.Counter()
    for saving, _, _ in cheats:
        if saving >= 100:
            saving_counts[saving] += 1

    # Output results
    if saving_counts:
        for saving, count in sorted(saving_counts.items()):
            print(f"There are {count} cheats that save {saving} picoseconds.")
    else:
        print("No cheats found that save at least 100 picoseconds.")

if __name__ == "__main__":
    solve_racetrack("20.txt")
