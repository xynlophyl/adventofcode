from collections import defaultdict
path = '12/sample_input.txt'
# path = '12/input.txt'

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
    
    # print((r,c), val, group)
    return group

def get_sides(group):
    group_set = set(group)

    horizontals = 0
    verticals = 0

    rs = [r for r,c in group]
    cs = [c for r,c in group]

    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)

    # check horizontal
    for r in range(min_r, max_r+2, 1):
        sections = []
        for c in range(min_c, max_c+1, 1):
            # print(r,c, lines[r][c], (r,c) in group_set, (r-1, c) in group_set)
            if ((r,c) in group_set) != ((r-1, c) in group_set):
                sections.append(1)
            else:
                sections.append(0)

        # print(sections)
        h = 0
        for idx, x in enumerate(sections[:-1]):
            if x == 1 and  sections[idx+1] == 0:
                h += 1
        if sections[-1] == 1:
            h += 1
        # print(h)
        horizontals += h
        # input()
    
    for c in range(min_c, max_c+2, 1):
        sections = []
        for r in range(min_r, max_r+1, 1):
            if ((r,c) in group_set) != ((r, c-1) in group_set):
                sections.append(1)
            else:
                sections.append(0)
        
        v = 0
        for idx, x in enumerate(sections[:-1]):
            if x == 1 and sections[idx+1] == 0:
                v += 1
        if sections[-1] == 1:
            v += 1
        verticals += v

    # print(horizontals, verticals)
    return horizontals + verticals

res = 0
visited = set()
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        if (r,c) in visited:
            continue
        group = get_group(r,c, val)
        area = len(group)
        sides = get_sides(group)
        print(r,c, val, area, sides)
        # input()
        res += area*sides

print(res)
# 893904