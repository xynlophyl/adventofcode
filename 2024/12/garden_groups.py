from collections import defaultdict
path = '12/sample_input.txt'
path = '12/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

"""PART 1"""
gardens = defaultdict(list)

dirs = [(0, 1), (-1, 0), (1,0), (0, -1)]
visited = set()

def get_area_perimeter(r,c, val):
    area = 0
    perimeter = 0
    stack = [(r,c)]
    while stack:
        r,c = stack.pop()

        if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[0]):
            perimeter += 1
            continue
        elif lines[r][c] != val:
            perimeter += 1
            continue
        elif (r,c) not in visited and lines[r][c] == val:
            area += 1
            visited.add((r,c))
        else:
            continue

        for dy, dx in dirs:
            stack.append((r+dy, c+dx))
    
    return area, perimeter

res = 0
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if (r,c) in visited:
                continue
        area, perimeter = get_area_perimeter(r, c, val)
        res += area*perimeter

print(res)

"""PART 2"""
is_valid = lambda r,c: 0 <= r < len(lines) and 0 <= c < len(lines[0])
def get_group(r, c, val):
    group = []
    stack = [(r,c)]

    while stack:
        r,c = stack.pop()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        group.append((r,c))

        for dy, dx in dirs:
            if is_valid(r+dy, c+dx) and lines[r+dy][c+dx] == val:
                stack.append((r+dy, c+dx))
    
    return group

def get_sides(group):
    group_set = set(group)

    rs = [r for r,c in group]
    cs = [c for r,c in group]

    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)

    # check top sides
    top = 0
    for r in range(min_r, max_r+1, 1):
        c = min_c
        while c <= max_c:
            if ((r,c) in group_set) and ((r-1, c) not in group_set):
                while c <= max_c and ((r,c) in group_set) and ((r-1, c) not in group_set):
                    c += 1
                top += 1
            else:
                c += 1
    
    # check bottom sides
    bottom = 0
    for r in range(min_r, max_r+1, 1):
        c = min_c
        while c <= max_c:
            if ((r,c) in group_set) and ((r+1, c) not in group_set):
                while c <= max_c and ((r,c) in group_set) and ((r+1, c) not in group_set):
                    c += 1
                bottom += 1
            else:
                c += 1

    # check left sides
    left = 0
    for c in range(min_c, max_c+1, 1):
        r = min_r
        while r <= max_r:
            if ((r,c) in group_set) and ((r, c-1) not in group_set):
                while r <= max_r and ((r,c) in group_set) and ((r, c-1) not in group_set):
                    r += 1
                left += 1
            else:
                r += 1
    
    # check right sides
    right = 0
    for c in range(min_c, max_c+1, 1):
        r = min_r
        while r <= max_r:
            if ((r,c) in group_set) and ((r, c+1) not in group_set):
                while r <= max_r and ((r,c) in group_set) and ((r, c+1) not in group_set):
                    r += 1
                right += 1
            else:
                r += 1
    return top+bottom+left+right

res = 0
visited = set()
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if (r,c) in visited:
            continue
        group = get_group(r,c, val)
        area = len(group)
        sides = get_sides(group)
        res += area*sides

print(res)