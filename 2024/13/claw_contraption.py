import functools
import numpy as np
import sys
sys.setrecursionlimit(15_000)

path = '13/sample_input.txt'
path = '13/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

def configure_machine(lines):
    machine = {}
    for line in lines[:2]:
        button, action = line.split(':')
        button = button[len('button '):]
        x, y = action.split(',')
        x = int(x[2:])
        y = int(y[2:])
        
        machine[button] = (x, y)

    prize_x, prize_y = lines[2][len('Prize: '):].split(',')
    prize_x = int(prize_x[2:])
    prize_y = int(prize_y[3:])

    machine['prize'] = (prize_x, prize_y)

    return machine

"""PART 1: dp"""
def get_score_dp(machine, increment = 0):
    @functools.cache
    def dp(x, y):
        if x < 0 or y < 0:
            return float('inf')
        elif x == 0 and y == 0:
            return 0
        else:
            return min(3+dp(x-a_x, y-a_y), 1+dp(x-b_x, y-b_y))
    
    a_x, a_y = machine["A"]
    b_x, b_y = machine["B"]
    
    prize_x, prize_y = machine["prize"]
    prize_x, prize_y = prize_x + increment, prize_y + increment

    score = dp(prize_x, prize_y)
    dp.cache_clear()
    return score

res = 0
for idx in range(0, len(lines), 4):
    machine = configure_machine(lines[idx:idx+3])
    score = get_score_dp(machine)
    # print('score', score)
    # input()
    if score != float('inf'):
        res += score

print(res)

"""PART 1 AND 2: numpy"""
is_close = lambda x, y = 0: x-y < 1e-2
def get_score_np(machine, increment = 0):

    machine_arr = np.array([machine["A"], machine["B"]]).T
    prize_arr = np.array([prize + increment for prize in machine["prize"]])

    counts = np.linalg.inv(machine_arr)@prize_arr

    

    if (is_close(counts[0]%1) or is_close(1-counts[0]%1)) and (is_close(counts[1]%1) or is_close(1-counts[1]%1)):
        return counts[0]*3 + counts[1]
    else:
        return 0
    
# part 1
res = 0
for idx in range(0, len(lines), 4):
    machine = configure_machine(lines[idx:idx+3])
    res += get_score_np(machine)

print(res)

# part 2
res = 0
for idx in range(0, len(lines), 4):
    machine = configure_machine(lines[idx:idx+3])
    res += get_score_np(machine, 10000000000000)

print(res)