import heapq

path = '16/sample_input.txt'
path = '16/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()
dirs = {
    1: lambda dy, dx: (dy, dx, 1),
    90: lambda dy, dx: (dx, -dy, 1000),
    -90: lambda dy, dx: (-dx, dy, 1000)
}

"""PART 1"""
def dijkstra(start, end):
    queue = [start]
    visited = set()

    while queue:
        cost, r, c, dy, dx = heapq.heappop(queue)
        if (r,c, dy, dx) in visited:
            continue
        elif (r,c) == end:
            return cost

        visited.add((r,c,dy,dx))
        
        for d, fn in dirs.items():
            nxt_dy, nxt_dx, nxt_cost = fn(dy, dx)
            # print(d, dy, dx, nxt_dy, nxt_dx)
            if d == 1:
                if lines[r+nxt_dy][c+nxt_dx] != '#':
                    heapq.heappush(queue, (cost+nxt_cost, r+dy, c+dx, nxt_dy, nxt_dx))
            else:
                heapq.heappush(queue, (cost+nxt_cost, r, c, nxt_dy, nxt_dx))

    return -1

start = None
end = None
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if val == 'S':
            start = (0, r, c, 0, 1)
        elif val == 'E':
            end = (r,c)
    if start is not None and end is not None:
        break 

r,c = start[1:3]
lines[r] = lines[r][:c] + '.' + lines[r][c+1:]
res = dijkstra(start, end)
print(res)

"""PART 2"""
def dijkstra(start, end):
    queue = [start]
    visited = {}
    all_paths = []
    best_cost = float('inf')

    while queue:
        cost, r, c, dy, dx, path = heapq.heappop(queue)
                    
        if cost > best_cost:
            return all_paths, best_cost
        elif (r,c,dy,dx) in visited and cost > visited[(r,c,dy,dx)]:
            continue
        elif (r,c) == end:
            all_paths.append(path)
            best_cost = min(best_cost, cost)
            continue
        else:
            visited[(r,c,dy,dx)] = cost

        for d, fn in dirs.items():
            nxt_dy, nxt_dx, nxt_cost = fn(dy, dx)
            # print(d, dy, dx, nxt_dy, nxt_dx)
            if d == 1:
                if lines[r+nxt_dy][c+nxt_dx] != '#':
                    heapq.heappush(
                        queue, 
                        (cost+nxt_cost, r+dy, c+dx, nxt_dy, nxt_dx, path+[(r,c)])
                    )

            else:
                heapq.heappush(
                    queue, 
                    (cost+nxt_cost, r, c, nxt_dy, nxt_dx, path+[(r,c)])
                )

    return [], -1

start = (*start, [])
all_paths, cost = dijkstra(start, end)

sitting_spots = set()
for path in all_paths:
    sitting_spots = sitting_spots | set(path)

res = len(sitting_spots) + 1
print(res)