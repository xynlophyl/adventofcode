path = '6/sample_input.txt'
path = '6/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

dirs = [(-1, 0), (0,1), (1,0), (0, -1)]

"""PART 1"""
def count_unique_locations(lines):
    # find guard
    visited = []
    x, y = None, None
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == '^':
                y, x = r, c
                break
        if x and y:
            break

    # predict traversal
    d = 0
    dy, dx = dirs[d]
    while 0 <= y+dy < len(lines) and 0 <= x+dx < len(row):
        visited.append((y,x))

        while lines[y+dy][x+dx] == '#':
            d = (d + 1)%4
            dy, dx = dirs[d]
        y += dy
        x += dx

    visited.append((y, x))
    res = len(set(visited))
    # print(visited)
    
    return res, visited

res, visited = count_unique_locations(lines)
print(res)


"""PART 2"""
def traverse(lines, start):
    y, x = start
    # predict traversal
    d = 0
    dy, dx = dirs[d]
    visit = set()
    while 0 <= y+dy < len(lines) and 0 <= x+dx < len(lines[0]):
        if (y, x, d) in visit: # cycle
            return 1
        visit.add((y, x, d))

        while lines[y+dy][x+dx] == '#':
            d = (d + 1)%4
            dy, dx = dirs[d]
        y += dy
        x += dx

    return 0
            
def find_num_loops(lines, visited):
    # find starting point
    x, y = None, None
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == '^':
                y, x = r, c
                break
        if x and y:
            break
    
    # brute force: place obstacle at every point along path and check for cycle
    res = 0
    for r, c in set(visited):
        val = lines[r][c]
        if val == '.':
            tmp = lines[r][:]
            lines[r] = lines[r][:c] + '#' + lines[r][c+1:]
            res += traverse(lines, (y,x))
            lines[r] = tmp

    return res

print(find_num_loops(lines, visited))