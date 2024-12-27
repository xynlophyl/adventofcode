from collections import Counter
import sys
sys.path.append('../')
from functions import get_day


path = f'{get_day(__file__)}/sample_input.txt'
# path = f'{get_day(__file__)}/input.txt'

with open(path, 'r') as f:
    text = f.read()
starts = [int(i) for i in text.splitlines()]

def mix_and_prune(prev, curr):
    res = prev^curr
    return res%16777216

"""PART 1"""
N = 2000
res = 0
# get ones of each secret number
all_ones = [[] for i in starts]
for idx, start in enumerate(starts):
    prev = start
    for i in range(N):
        # print(prev)
        # step 1
        curr = prev*64
        curr = mix_and_prune(prev, curr)

        # step 2
        curr, prev = curr//32, curr
        curr = mix_and_prune(prev, curr)

        # step 3
        curr, prev = curr*2048, curr
        curr = mix_and_prune(prev, curr)
        prev = curr
    
        all_ones[idx].append(curr%10)

    res += curr
print(res)

"""PART 2"""
def get_sequences_values(ones, changes, window_size = 4):
    sequence_val = {}
    idx = 0
    while idx < N - window_size:
        sequence = (*changes[idx:idx+window_size],)
        if sequence not in sequence_val:
            sequence_val[sequence] = ones[idx+window_size-1]

        idx += 1
        
    return sequence_val

all_changes = []
res = 0

counter = Counter()
for idx, ones in enumerate(all_ones):
    changes = [0] + [ones[idx+1] - ones[idx] for idx in range(N-1)]

    for seq, val in get_sequences_values(ones, changes).items():
        counter[seq] += val
    
res = max(counter.values())
print(res)
# res < 1786

seq, val = max(counter.items(), key = lambda x: x[1])
print(seq, val)

"""
1. x*64 => mix => prune => x1
2. x1//32 => mix => prune => x2
3. x2*2048 => mix => prune => res

mix(x,y) = x^y 
prune(x) = x%16777216
"""