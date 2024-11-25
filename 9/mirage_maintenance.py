import numpy as np

def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = mirage_maintenance(lines)
        res2 = mirage_maintenance2(lines)

    return res1, res2

def mirage_maintenance(lines):

    res = 0

    for l in lines:
        vals = [int(val) for val in l.split(' ')]

        next_val = vals[-1] + compute_difference(vals)

        res += next_val
    return res

def compute_difference(vals):

    if vals == [0]*len(vals):

        return 0
    
    diffs = [vals[i+1] - vals[i] for i in range(len(vals)-1)]

    next_diff = compute_difference(diffs)

    # print(diffs[-1] + next_diff)

    return diffs[-1] + next_diff


def mirage_maintenance2(lines):

    res = 0

    for l in lines:
        vals = [int(val) for val in l.split(' ')]

        next_val = vals[0] - compute_difference2(vals)

        res += next_val
    return res

def compute_difference2(vals):

    if vals == [0]*len(vals):

        return 0
    
    diffs = [vals[i+1] - vals[i] for i in range(len(vals)-1)]

    next_diff = compute_difference2(diffs)

    # print(diffs[-1] + next_diff)

    return diffs[0] - next_diff






if __name__ == '__main__':

    print(main())