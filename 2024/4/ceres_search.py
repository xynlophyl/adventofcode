import sys
sys.path.append('../')
from functions import read_file, print_answers

def find_X_MAS(lines):
    queue = []
    
    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == 'A':
                queue.append((r,c))

    d = [(1,1), (1,-1)]

    res = 0
    for r, c in queue:
        for dx, dy in d:
            if 0 <= r+dy < len(lines) and 0 <= c+dx < len(lines[0]) and 0 <= r-dx < len(lines) and 0 <= c-dy < len(lines[0]):
                x = lines[r+dy][c+dx]
                y = lines[r-dy][c-dx]

                if x in 'MS' and y in 'MS' and x != y:
                    continue
                else:
                   break
            else:
                break
        else:
            res += 1

    return res

def find_XMAS(lines):
    queue = []
    order = 'xmas'.upper()

    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val == 'X':
                queue.append((r,c))

    res = 0
    d =[(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1, 1), (-1, -1)]

    for dx, dy in d:
        for r, c in queue:
            idx = 0

            while 0 <= r+dy < len(lines) and 0 <= c+dx < len(lines[0]) and idx+1 < len(order) and lines[r+dy][c+dx] == order[idx+1]:
                idx += 1
                r = r+dy
                c = c+dx
            
            if idx +1 == 4:
                res += 1
    
    return res

def main(path):

    text = read_file(path)

    lines = text.splitlines()

    lines = [line.strip() for line in lines]
    lines = [[x for x in line] for line in lines]

    ans1 = find_XMAS(lines)
    ans2 = find_X_MAS(lines)

    print_answers(path, ans1, ans2)

main('4/sample_input.txt')
main('4/input.txt')
