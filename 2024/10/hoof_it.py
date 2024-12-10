from collections import deque, defaultdict
path = '10/sample_input.txt'
path = '10/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()
lines = [[int(val) for val in line] for line in lines]

"""PART 1"""
queue = deque([])
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val == 0:
            queue.append(((r,c), (r,c), val))

dirs = [(0,1), (0,-1), (-1,0), (1,0)]
count = 0
visited = defaultdict(set)
while queue:
    parent, (r, c), val = queue.popleft()
    if (r,c) not in visited[parent] and val == 9:
        visited[parent].add((r,c))
        count += 1
        continue
    for dy, dx in dirs:
        if 0<=r+dy<len(lines) and 0 <= c+dx<len(row) and lines[r+dy][c+dx] == val+1:
            queue.append((parent,(r+dy, c+dx), val+1))

print(count)

"""PART 2"""
queue = deque([])
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val == 0:
            queue.append(((r,c), (r,c), val))

dirs = [(0,1), (0,-1), (-1,0), (1,0)]
count = 0
visited = defaultdict(int)
while queue:
    parent, (r, c), val = queue.popleft()
    if val == 9:
        visited[(parent, (r,c))] += 1
        continue
    for dy, dx in dirs:
        if 0<=r+dy<len(lines) and 0 <= c+dx<len(row) and lines[r+dy][c+dx] == val+1:
            queue.append((parent, (r+dy, c+dx), val+1))

res = 0
for route, count in visited.items():
    res += count

print(res)