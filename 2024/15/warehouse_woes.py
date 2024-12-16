from collections import deque
import sys
sys.setrecursionlimit(50_000)
path = '15/sample_input.txt'
path = '15/input.txt'

with open(path, 'r') as f:
    text = f.read()

original_grid, actions = text.split('\n\n')
grid = [[val for val in line] for line in original_grid.splitlines()]
actions = actions.replace('\n','')

dirs = {
    '>': (0,1),
    'v': (1,0),
    '^': (-1,0),
    '<': (0, -1)
}

### PART 1 ###
def push_wall(r, c, dy, dx):
    end_r, end_c = r+dy, c+dx
    while True:
        val = grid[end_r][end_c]
        if val == 'O':
            end_r, end_c = end_r + dy, end_c + dx
        else:
            if val == '#':
                return r,c
            elif val == '.':
                return end_r, end_c
            else: # symbol not found
                print('PUSH WALL: unknown symbol', grid[end_r][end_c])
                return float('inf'), float('inf')

def follow_actions(r, c, action_idx):
    if action_idx >= len(actions):
        return 
    
    action = actions[action_idx]

    dy, dx = dirs[action]

    val = grid[r+dy][c+dx]
    if val == '#': # hit solid wall, no movement
        pass
    elif val == '.': # move into empty space
        grid[r][c], grid[r+dy][c+dx] = '.', '@'
        r, c = r+dy, c+dx
    elif val == 'O': # hit moveable wall
        end_r, end_c = push_wall(r, c, dy, dx)
        if (r, c) != (end_r, end_c): # if 'O' is not against a solid wall, move it across
            grid[r][c], grid[r+dy][c+dx], grid[end_r][end_c] = '.', '@', 'O'
            r, c = r+dy, c+dx
    else:
        print('FOLLOW ACTIONS: unknown symbol', val)

    follow_actions(r, c, action_idx+1)

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == '@':
            follow_actions(r,c, 0)
            break

res = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == 'O':
            res += 100*r+c

print(res)

### PART 2 ###
add_other_wall = lambda r,c: (r, c+1) if grid[r][c] == '[' else (r, c-1)
def push_wall(r, c, dy, dx):
    end_r, end_c = r+dy, c+dx
    visited = set()
    all_walls = []
    
    if dy != 0: # pushing vertically
        # add starting wall
        queue = deque([(end_r, end_c), add_other_wall(end_r, end_c)])
        while queue:
            wall_r, wall_c = queue.popleft()
            if (wall_r, wall_c) in visited:
                continue
            visited.add((wall_r, wall_c))
            all_walls.append((wall_r, wall_c))

            val = grid[wall_r+dy][wall_c]
            if val == '#':
                return r, c, []
            elif val in ('[', ']'):
                queue.append((wall_r+dy, wall_c))
                queue.append(add_other_wall(wall_r+dy, wall_c))
            elif val == '.':
                continue
        return float('inf'), float('inf'), all_walls

    else: # pushing horizontally
        while True:
            val = grid[end_r][end_c]
            if val == '.':
                return float('inf'), float('inf'), all_walls
            elif val == '#':
                return r, c, []
            elif val in ('[',']'):
                all_walls.append((end_r, end_c))
                visited.add((end_r, end_c))
                end_r, end_c = end_r + dy, end_c + dx
            else:
                print('PUSH WALL H: unknown symbol', val)
                return float('inf'), float('inf'), []            

def follow_actions(r, c, action_idx):
    if action_idx >= len(actions):
        return

    action = actions[action_idx]
    dy, dx = dirs[action]

    # for row in grid:
    #     print(''.join(row))
    # print(action, f'{action_idx}/{len(actions)}')
    # input()

    val = grid[r+dy][c+dx]
    if val == '#': # solid wall
        # print('solid wall')
        pass
    elif val == '.': # empty space
        # print('empty space')
        grid[r][c], grid[r+dy][c+dx] = '.', '@'
        r, c = r+dy, c+dx
    elif val in ('[', ']'): # pushable wall
        # print('pushable wall')
        end_r, end_c, walls = push_wall(r, c, dy, dx)
        if (r,c) != (end_r, end_c):
            # print(walls)
            if walls: 
                for wall_r, wall_c in reversed(walls):
                    grid[wall_r+dy][wall_c+dx], grid[wall_r][wall_c] = grid[wall_r][wall_c], '.'
                grid[r][c], grid[r+dy][c+dx] = '.', '@' # shift lanternfish
                r, c = r+dy, c+dx
    else:
        print('FOLLOW ACTIONS: unknown symbol', val)

    follow_actions(r, c, action_idx + 1)

# expand grid
grid = []
for row in original_grid.splitlines():
    expanded_row = []
    for val in row:
        if val in ('#', '.'):
            expanded_row += [val, val]
        elif val == 'O':
            expanded_row += ['[', ']']
        elif val == '@':
            expanded_row += ['@', '.']
        else:
            print('EXPAND GRID: unknown symbol', val)

    # print(expanded_row)
    grid.append(expanded_row)

flag = False
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == '@':
            follow_actions(r, c, action_idx=0)
            flag = True
            break
    if flag:
        break
res = 0
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == '[':
            res += 100*r+c

# for row in grid:
#     print(''.join(row))
print(res)