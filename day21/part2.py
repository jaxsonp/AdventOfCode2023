"""
------------- INCOMPLETE :( --------
current brute force solution is way to slow

"""

from collections import deque

with open("day21/test_input", "r") as f:
    map = [[c for c in line.strip()] for line in f.readlines()]

N_STEPS = 1000
W = len(map[0])
H = len(map)
start_x = -1
start_y = -1
for y in range(H):
    for x in range(W):
        if map[y][x] == 'S':
            start_x = x
            start_y = y
assert(start_x != -1 and start_y != -1)
print(f"Starting at {start_x}, {start_y}")

end_positions = set()

q = deque()
q_set = set()
q.append((start_x, start_y, N_STEPS))
q_set.add((start_x, start_y, N_STEPS))

while len(q) > 0:
    x_pos, y_pos, steps_left = q.popleft()

    if steps_left == 0:
        end_positions.add((x_pos, y_pos))
        continue

    for neighbor_x, neighbor_y in [(x_pos, y_pos-1), (x_pos+1, y_pos), (x_pos, y_pos+1), (x_pos-1, y_pos)]:

        if map[neighbor_y % H][neighbor_x % W] != '#':
            if (neighbor_x, neighbor_y, steps_left - 1) in q_set:
                continue
            q.append((neighbor_x, neighbor_y, steps_left - 1))
            q_set.add((neighbor_x, neighbor_y, steps_left - 1))

print(f"There are {len(end_positions)} end positions")