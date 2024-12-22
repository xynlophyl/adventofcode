from collections import deque, Counter
from tqdm import tqdm
import sys
sys.path.append('../')
from functions import get_day


path = f'{get_day(__file__)}/sample_input.txt'
# path = f'{get_day(__file__)}/input.txt'

with open(path, 'r') as f:
    text = f.read()

grid = text.splitlines()

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == 'S':
            start = (r,c)
        if val == 'E':
            end = (r,c)

def visualize(grid, path, cheats = [], nxt = (-1,-1)):
    print('   ', ''.join([str((i)%10) for i in range(len(grid[0]))]))
    grid = grid[:]

    for r,c in path:
        grid[r] = grid[r][:c] + 'O' + grid[r][c+1:]

    if nxt != (-1, -1):
        r,c = nxt
        grid[r] = grid[r][:c] + 'O' + grid[r][c+1:]

    for idx, (r,c) in enumerate(cheats):
        grid[r] = grid[r][:c] + str(idx+1) + grid[r][c+1:]

    for idx, row in enumerate(grid):
        print(idx, ' '*(2-len(str(idx))), row)


dirs = [(0,1), (1,0), (0,-1), (-1,0)]
is_valid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])

def get_dists(start):
    dists = {}
    queue = deque([start])
    visited = set()

    while queue:
        r, c, dist = queue.popleft()

        if (r,c) in visited:
            continue
        visited.add((r,c))

        dists[(r,c)] = dist

        for dy, dx in dirs:
            if not is_valid(r+dy, c+dx) or grid[r+dy][c+dx] == '#':
                continue
            queue.append((r+dy,c+dx, dist+1))

    return dists

def search_with_cheats(start, num_cheats):
    queue = []
    r, c = start
    for dy, dx in dirs:
        if is_valid(r+dy, c+dx) and grid[r+dy][c+dx] == '#':
            queue.append((r+dy, c+dx, 1, (r+dy, c+dx)))

    dists = {}
    queue = deque(queue)
    while queue:
        r, c, dist, cheat_start = queue.popleft()
        cheats = (*cheat_start, r,c)
        if cheats in dists:
            continue
        dists[cheats] = dist

        if dist == num_cheats:
            continue

        for dy, dx in dirs:
            if not is_valid(r+dy, c+dx):
                continue
            elif dist == num_cheats-1 and grid[r+dy][c+dx] !='#': # make sure that the final timestep of cheating brings racecar back to track
                queue.append((r+dy, c+dx, dist+1, cheat_start))
            else:
                queue.append((r+dy,c+dx, dist+1, cheat_start))
    
    return dists

def count_time_saves(num_cheats, threshold):
    res = 0
    counter = Counter()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '#' or (r,c) not in dists_from_start:
                continue
            cheat_ends = search_with_cheats((r,c), num_cheats)

            a = max(cheat_ends.values())
            print(a)

            for (_, _, cheat_r, cheat_c), dist in cheat_ends.items():
                if (cheat_r, cheat_c) not in dists_from_end:
                    continue
                total_dist = dists_from_start[(r,c)] + dist + dists_from_end[(cheat_r,cheat_c)]-1
                if original_dist - total_dist >= threshold:
                    counter[original_dist-total_dist] += 1
                    res += 1
    
    for i, j in sorted(counter.items(), key = lambda x: x[0]):
        print(j, i)

    return res

dists_from_start = get_dists((*start, 1))
dists_from_end = get_dists((*end, 1))
original_dist = dists_from_start[end]

"""PART 1"""
# res = count_time_saves(2, 1)
# res = count_time_saves(2, 100)
# print(res)
print()

"""PART 2"""
res = count_time_saves(20, 50)

# res = count_time_saves(20, 100)
print(res)
# 140084 < res < 1759777 < 2199963 

# """PART 1"""
# dirs = [(0,1), (1,0), (0,-1), (-1,0)]
# is_valid = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
# def search(start, end):
#     queue = deque([start])
#     visited = set()

#     while queue:
#         r, c, path = queue.popleft()

#         if (r,c) == end:
#             return path
#         elif (r,c) in visited:
#             continue        
#         visited.add((r,c))

#         for dy, dx in dirs:
#             if is_valid(r+dy, c+dx) and grid[r+dy][c+dx] !='#':
#                 queue.append((r+dy,c+dx, path+[(r,c)]))

# # # find original path        
# # path = search((*start, []), end)
# # print('original length', len(path))

# # counter = Counter()
# # for idx, (r,c) in tqdm(enumerate(path), total = len(path)):
# #     for dy, dx in dirs:
# #         if grid[r+dy][c+dx] == '#':
# #             new_path = search([r+dy,c+dx, path[:idx]], end)
# #             counter[len(path) - len(new_path)-1] += 1

# # res = 0
# # for saved_time, count in counter.items():
# #     if saved_time >= 100:
# #         res += count

# # print(res)