from collections import deque, Counter
from tqdm import tqdm
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
    (0,1): '>',
    (1,0): 'v',
    (0,-1): '<',
    (-1,0): '^', 
    (0,0):''
}

get_vector = lambda diff: (abs(diff), (diff)//abs(diff) if diff != 0 else 0)
def find_sequence(code):
    def find(code, positions):
        empty_cell = positions[' ']
        r, c = positions['A']
        prev_dy, prev_dx = 0, 0

        sequence = ''

        for val in code:
            assert val in positions
            y, x = positions[val]

            # calculate magnitude and direction between current position and next position
            dy, dir_y = get_vector(y-r)
            dx, dir_x = get_vector(x-c)

            # print(val, (r, c), (y, x), (dy, dir_y), (dx, dir_x))

            if r == empty_cell[0]: # if the arm is currently on the same row as the empty space, move out the way with vertical action first
                sequence += actions[(dir_y, 0)]*dy
                sequence += actions[(0, dir_x)]*dx
            elif c == empty_cell[1]: # if the arm is currently on the same col as the empty space, move out the way with horizontal action first
                sequence += actions[(0, dir_x)]*dx
                sequence += actions[(dir_y, 0)]*dy
            else:
                sequence += actions[(dir_y, 0)]*dy
                sequence += actions[(0, dir_x)]*dx

            sequence += 'A'

            # update prev
            r, c = y, x
            prev_dy, prev_dx = dy, dx

        return sequence

    # code: what robot1 needs to type into numpad = 029A
    # get sequence for robot 1 to enter code
    print('code', code)
    sequence = find(code, num_positions)
    sequence0 = sequence[:]
    print('seq1', sequence, len(sequence))
    
    # get sequence for robot 2 to instruct robot 1
    sequence = find(sequence, dir_positions)
    sequence1 = sequence[:]
    print('seq2', sequence, len(sequence))

    # get sequence for me to instruct robot 2
    sequence = find(sequence, dir_positions)
    print('seq3', sequence, len(sequence))
    print()

    # for i, j in zip(sequence1, sequence.split('A')):
    #     print(i, j)

    return sequence

res = 0
for code in lines:
    sequence = find_sequence(code)
    res += int(code[:-1])*len(sequence)

print(res)
# res < 171460

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

for s3 in ['<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A']:
    s2 = visualize(s3, dir_positions, dir_grid)
    s1 = visualize(s2, dir_positions, dir_grid)
    code = visualize(s1, num_positions, num_grid)

    print('code', code, len(code))
    print('seq1', s1, len(s1))
    print('seq2', s2, len(s2))
    print('seq3', s3, len(s3))