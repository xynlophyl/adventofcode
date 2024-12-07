path = '7/sample_input.txt'
path = '7/input.txt'

import time
start = time.time()

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

def backtrack(answer, part, idx, res):

    if idx == len(part):
        return res == answer

    for operation in operations:
        if backtrack(answer, part, idx = idx + 1, res = operation(res, part[idx])):
            return True

    return False

answers, parts = parse_lines(lines)

res = 0
for answer, part in zip(answers, parts):
    if backtrack(answer, part, idx = 1, res = part[0]):
        # print('YES', answer)
        res += answer

print(res, time.time() - start)

"""PART 2"""
operations = [
    lambda x, y: x+y,
    lambda x, y: x*y,
    lambda x, y: int(str(x) + str(y)) 
]
res = 0
for answer, part in zip(answers, parts):
    if backtrack(answer, part, idx = 1, res = part[0]):
        res += answer

print(res, time.time() - start)
