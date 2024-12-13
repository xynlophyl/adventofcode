import functools
path = '13/sample_input.txt'
path = '13/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

"""PART 1"""
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
        
'''def get_counts_for_prize(machine):

    """OPT on cost
    does not work, since heuristic for min function (prize_x + prize_y) does not take into account how much of each is left, 
    so it will just prioritize the option that has the best movement per cost
    this means that it will eventually reach the lower of the two coordinates, and be forced to go negative
    """

    a_x, a_y = machine["A"]
    b_x, b_y = machine["B"]
    prize_x, prize_y = machine["prize"]
    
    print('machine', a_x, a_y, b_x, b_y, prize_x, prize_y)
    
    max_a = max(prize_x // a_x, prize_y // a_y)
    max_b = max(prize_x // b_x, prize_y // b_y)

    import numpy as np
    opt = np.array(
        [(-1, -1, -1, -1) for i in range(max(max_a, max_b))]
    )

    opt[0] = (0, 0, prize_x, prize_y)
    
    for idx in range(1, len(opt)):
        if idx <= 3:
            a, b, x, y = opt[idx-1]
            opt[idx] = (a, b+1, x-b_x, y-b_y)
        else:

            a1, b1, x1, y1 =  opt[idx-1]
            a3, b3, x3, y3 = opt[idx-3]

            new1 = (a1, b1+1, x1-b_x, y1-b_y)
            new3 = (a3+1, b3, x3-a_x, y3-a_y)

            if (new1[-1] == 0 and new1[-2] == 0) or (new3[-1] < 0 or new3[-2] < 0):
                opt[idx] = new1
            elif (new1[-1] < 0 or new1[-2] < 0) or (new3[-1] == 0 and new3[-2] == 0):
                opt[idx] = new3
            else:
                print('test')
                opt[idx] = min(
                    new1,
                    new3,
                    key = lambda val: val[-1] + val[-2]
                )
            print('chosen', opt[idx])
        input()
    print(opt[-1])

    if opt[-1][-1] == 0:
        return opt[:2]
    else:
        return -1, -1'''

def get_score(machine):
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

    print('machine', a_x, a_y, b_x, b_y, prize_x, prize_y)

    score = dp(prize_x, prize_y)
    dp.cache_clear()
    return score
        

res = 0
for idx in range(0, len(lines), 4):
    machine = configure_machine(lines[idx:idx+3])
    score = get_score(machine)
    # print('score', score)
    # input()
    if score != float('inf'):
        res += score

print(res)

# 38839 + 