import functools
import sys
sys.path.append('../')
from functions import get_day

path = f'{get_day(__file__)}/sample_input.txt'
path = f'{get_day(__file__)}/input.txt'

with open(path, 'r') as f:
    text = f.read()

towels, patterns = text.split('\n\n')
towels = towels.split(', ')
patterns = patterns.splitlines()

# print('towels', towels)

"""PART 1"""
def check_pattern(pattern):
    def search(idx):
        
        if idx == len(pattern):
            return 1
    
        for towel in towels:
            if towel == pattern[idx:idx+len(towel)]:
                if search(idx + len(towel)):
                    return 1
                
        
        return 0

    pattern = pattern
    return search(0)

res = 0
for pattern in patterns:
    res += check_pattern(pattern)

print(res)

"""PART 2"""
def count_arrangements(pattern):
    @functools.cache
    def search(idx):
        
        if idx == len(pattern):
            return 1
    
        count = 0 
        for towel in towels:
            if towel == pattern[idx:idx+len(towel)]:
                count += search(idx + len(towel))
            
        return count

    pattern = pattern
    return search(0)

res = 0
for pattern in patterns:
    res += count_arrangements(pattern)
print(res)