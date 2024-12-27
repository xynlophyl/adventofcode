from collections import deque
import sys
sys.path.append('../')
from functions import get_day

path = f'{get_day(__file__)}/sample_input.txt'
# path = f'{get_day(__file__)}/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

def get_position_mappings(grid):
    positions = {}

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            positions[val] = (r,c)

    return positions

num_grid = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [' ','0','A']    
]
num_positions = get_position_mappings(num_grid)

dir_grid = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]
dir_positions = get_position_mappings(dir_grid)

actions = {
    (-1,0): '^', 
    (0,1): '>',
    (1,0): 'v',
    (0,-1): '<',
    (0,0): ''
}

# def search(code, version):
#     grid = dir_grid if version == 1 else num_grid
#     r, c = (0,2) if version == 1 else (3,2)

#     queue = deque([(r,c, '', 0, '')])
#     all_sequences = []

#     visited = set()
#     while queue:
#         r, c, sequence, idx, last_action = queue.popleft()
        
#         nxt_idx = idx
#         if idx == len(code):
#             all_sequences.append(sequence+last_action)
#             continue
#         elif grid[r][c] == ' ':
#             continue
#         elif code[idx] == grid[r][c]:
#             last_action += 'A'
#             nxt_idx += 1
#         elif (r,c,idx,last_action) in visited:
#             continue
#         visited.add((r,c,idx,last_action))

#         for (dy, dx), action in actions.items():
#             if not( 0 <= r+dy < len(grid) and 0 <= c+dx < len(grid[0])):
#                 continue
#             queue.append((r+dy, c+dx, sequence+last_action, nxt_idx, action))

#     return all_sequences

# res = 0
# for code in lines[2:3]:
#     low = float('inf')
#     best1 = best2 = best3 = None
#     for sequence1 in search(code, 0):
#         for sequence2 in search(sequence1, 1):
#             for sequence3 in search(sequence2, 1):
#                 if len(sequence3) < low:
#                     best1 = sequence1
#                     best2 = sequence2
#                     best3 = sequence3
#                     low = len(sequence3)

#     print('code', code)
#     print('seq1', best1, len(best1))
#     print('seq2', best2, len(best2))
#     print('seq3', best3, len(best3))
#     print()

#     res += int(code[:-1])*low

# print(res)

def get_sequence(code, version):
    def search(r,c, idx, path, visited):
        # print(len(visited), len(path))

        nxt_idx = idx
        if idx == len(code):
            return [''.join(path)]
        elif grid[r][c] == code[idx]:
            path += 'A'
            nxt_idx += 1
        elif (r,c,idx) in visited:
            return -1
        visited.add((r,c, idx))

        all_paths = []
        for (dy, dx), action in actions.items():
            if not (0 <= r+dy < len(grid) and 0 <= c+dx < len(grid[0])):
                continue

            paths = search(r+dy, c+dx, nxt_idx, path+action, visited)
            if paths == -1:
                continue

            all_paths += paths

        # visited.remove((r,c,idx))
        return all_paths
    
    grid = dir_grid if version == 1 else num_grid
    r, c = (0,2) if version == 1 else (3,2)
    
    all_sequences = search(r, c, 0, path = '', visited = set())
    return all_sequences

res = 0
for code in lines[2:3]:
    low = float('inf')
    best1 = best2 = best3 = None
    for sequence1 in get_sequence(code, 0):
        print(sequence1, len(sequence1))
        for sequence2 in get_sequence(sequence1, 1):
            for sequence3 in get_sequence(sequence2, 1):
                if len(sequence3) < low:
                    best1 = sequence1
                    best2 = sequence2
                    best3 = sequence3
                    low = len(sequence3)
    print('code', code)
    print('seq1', best1, len(best1))
    print('seq2', best2, len(best2))
    print('seq3', best3, len(best3))
    print()

    res += int(code[:-1])*low
print(res)  

def visualize(sequence, positions, grid):
    actions_rev = {val: key for key, val in actions.items()}
    r, c = positions['A']

    code = ''
    for val in sequence:
        if val == 'A':
            code += grid[r][c]
            continue

        dy, dx = actions_rev[val]
        r, c = r+dy, c+dx

    return code

for s3 in ['<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A', sequence3]:
    s2 = visualize(s3, dir_positions, dir_grid)
    s1 = visualize(s2, dir_positions, dir_grid)
    code = visualize(s1, num_positions, num_grid)

    print('code', code, len(code))
    print('seq1', s1, len(s1))
    print('seq2', s2, len(s2))
    print('seq3', s3, len(s3))
    print()
    
