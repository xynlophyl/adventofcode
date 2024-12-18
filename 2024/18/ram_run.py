from collections import deque
path = '18/sample_input.txt'
n = 7
path = '18/input.txt'
n = 71

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

original_grid = ['.'*n]*n
def generate_grid(grid, stop):
    for idx, line in enumerate(lines):
        if idx == stop:
            break
        r, c = line.split(',')
        r, c = int(r), int(c)

        grid[r] = grid[r][:c] + '#' + grid[r][c+1:]

    return grid

grid = generate_grid(original_grid, 1024)

"""PART 1"""
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
is_valid = lambda y,x: 0 <= y < len(grid) and 0 <= x < len(grid[0])
def find_path(start):
    queue = deque([start])

    visited = set()
    while queue:
        r, c, path = queue.popleft()
        
        if (r,c) == (n-1,n-1):
            return path
        elif (r,c) in visited:
            continue

        visited.add((r,c))
        
        for dy, dx in dirs:
            if is_valid(r+dy, c+dx) and grid[r+dy][c+dx] !='#':
                queue.append((r+dy,c+dx,path+[(r,c)]))

    return []

path = find_path((0,0,[]))
res = len(path)
print(res)

"""PART 2"""
grid = original_grid[:]
path = find_path((0,0, []))
for res, line in enumerate(lines):
    r, c = line.split(',')
    r, c = int(r), int(c)

    # update grid
    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
    
    # if new obstacle obstructs previous shortest path, then find a new path starting from right before block
    if (r,c) in path:
        start = path.index((r,c))
        
        start_r, start_c = path[start-1]
        path = find_path((start_r, start_c, path[:start]))

        # if no new path, then get result
        if path == []:
            break

res = f"{r},{c}"
print(res)
