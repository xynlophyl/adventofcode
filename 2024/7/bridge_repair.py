import functools
import time
start = time.time()

path = '7/sample_input.txt'
path = '7/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

"""PART 1"""
def parse_lines(lines):
    answers = []
    parts = []

    for line in lines:
        answer, part = line.split(':')
        pts = [int(p) for p in part.split()]

        answers.append(int(answer))
        parts.append(pts)

    return answers, parts

operations = [
    lambda x, y: x+y,
    lambda x, y: x*y,
]

def evaluate(answer, part):
    @functools.cache
    def backtrack(idx, res):
        if idx == len(part):
            return res == answer

        for operation in operations:
            if backtrack(idx+1, operation(res, part[idx])):
                return True

    return backtrack(0, 0)

answers, parts = parse_lines(lines)

res = 0
for answer, part in zip(answers, parts):
    res += answer if evaluate(answer, part) else 0
        
print(res, time.time()-start)

"""PART 2"""
operations.append(lambda x, y: int(str(x) + str(y)))
res = 0
for answer, part in zip(answers, parts):
    res += answer if evaluate(answer, part) else 0

print(res, time.time()-start)
