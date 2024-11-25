from collections import deque

next_enter_dir = {
    (1,0): 0, # entering neighbor from above
    (-1,0): 1, # from below
    (0, 1): 2, # from left
    (0, -1): 3 # from right
}

dirs = {
    '|': [(1,0), (-1,0), (0,0), (0,0)],
    '-': [(0,0), (0,0), (0,1), (0,-1)],
    'L': [(0,1), (0,0), (0,0), (-1,0)],
    'J': [(0,-1), (0,0), (-1,0), (0,0)],
    '7': [(0,0), (0,-1), (1,0), (0,0)],
    'F': [(0,0), (0,1), (0,0), (1,0)],
}

def main():

    path = './input.txt'
    # path = './sample_input.txt'
    # path = './sample_input2.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1, explored = pipe_maze(lines)
        res2 = pipe_maze2(lines, explored)

    return res1, res2

def pipe_maze(lines):

    start_y, start_x = find_start(lines)

    queue = deque([(start_y, start_x, -1, 0)])

    explored = {}

    while queue:

        y, x, enter_dir, dist = queue.popleft()

        if (y,x) in explored: 

            return dist, explored

        explored[(y,x)] = dist

        for (new_y, new_x, new_enter_dir) in get_neighbors(lines, y, x, enter_dir):

            if dist - explored.get((new_y, new_x), -2) == 1: continue

            queue.append((new_y, new_x, new_enter_dir, dist + 1))

    return -1

def find_start(lines):

    for i, line in enumerate(lines):

        if 'S' in line: return (i, line.index('S'))

def get_neighbors(lines, r, c, enter_dir):

    # defining UDLR index mapping for how the animal is entering the neighboring pipe 
    # (i.e. if animal leaves current pipe from the right -> it will enter the neighboring pipe from the left)

    neis = []

    curr = lines[r][c]

    if curr == 'S':

        for (dy, dx), next_dir in next_enter_dir.items():

            if (r + dy) >= len(lines) or (r + dy) < 0 or (c + dx) >= len(lines[0]) or (c + dx) < 0: continue

            elif lines[r+dy][c+dx] == '.': continue

            elif dirs[lines[r+dy][c+dx]][next_dir] == (0,0): continue

            neis.append((r+dy, c+dx, next_enter_dir[(dy, dx)]))

    else:
    
        dy, dx = dirs[curr][enter_dir]

        if not ((dy,dx) == (0,0) or r + dy >= len(lines) or r + dy < 0 or c + dx >= len(lines) or c + dx < 0 or lines[r+dy][c+dx] == '.'):

            neis.append((r+dy, c+dx, next_enter_dir[(dy, dx)]))

    return neis

def pipe_maze2(lines, explored):

    loop = only_loop(lines, explored)

    path = get_loop(loop)

    path_area = shoelace_formula(path)

    return picks_theorem(path_area, len(path))


def only_loop(lines, explored):

    for r in range(len(lines)):

        for c in range(len(lines[0])):

            if (r,c) not in explored:

                lines[r] = lines[r][:c] + '.' + lines[r][c+1:]

    return lines

def get_loop(loop):

    y, x = find_start(loop)
    path = []
    explored = set()
    next_dir = -1

    while True:

        if (y,x) in explored: return path

        explored.add((y,x))
        path.append((y,x))

        curr = loop[y][x]

        if curr == 'S':

            if y-1 >= 0 and loop[y-1][x] in '|F7':

                dy, dx = -1, 0
            
            elif y+1 < len(loop) and loop[y+1][x] in '|JL':

                dy, dx = 1, 0

            elif x-1 >= 0 and loop[y][x-1] in '-FL':

                dy, dx = 0, -1

            elif x+1 < len(loop[0]) and loop[y][x+1] in '-J7':

                dy, dx = 0, 1

        else:
            
            dy, dx = dirs[curr][next_dir]
        
        y, x = y + dy, x + dx
        next_dir = next_enter_dir[(dy,dx)]

def shoelace_formula(path):

    area = 0

    for i in range(len(path)):

        area += path[i][0]*path[i-1][1] - path[i-1][0]*path[i][1]

    return 0.5*abs(area)

def picks_theorem(area, path_len):

    return int(area - 0.5*path_len + 1)


        

if __name__ == '__main__':

    print(main())