import re
from collections import Counter

path = '14/sample_input.txt'
dims = (7,11)
path = '14/input.txt'
dims = (103,101)

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

positions = {}
velocities = {}
for idx, line in enumerate(lines):
    robot_regex = re.compile(r"p=(.?\d+),(.?\d+) v=(.?\d+),(.?\d+)")
    robot = re.match(robot_regex, line)

    p = int(robot.group(2)), int(robot.group(1))
    v = int(robot.group(4)), int(robot.group(3))

    positions[idx] = p
    velocities[idx] = v

def move(positions, time):
    positions = {
        idx: (
            (positions[idx][0]+time*velocities[idx][0])%dims[0], 
            (positions[idx][1]+time*velocities[idx][1])%dims[1]
        ) for idx in positions.keys()
    }

    return positions

"""PART 1"""
# move robots
positions = move(positions, 100)
counter = Counter()
for y,x in positions.values():
    counter[(y,x)] += 1

# calculate quadrants
y_half, x_half = dims[0]//2, dims[1]//2
q1 = 0
for y in range(y_half):
    for x in range(x_half):
        q1 += counter[(y,x)]

q2 = 0
for y in range(y_half):
    for x in range(x_half+1, dims[1]):
        q2 += counter[(y,x)]

q3 = 0
for y in range(y_half+1, dims[0]):
    for x in range(x_half):
        q3 += counter[(y,x)]

q4 = 0
for y in range(y_half+1, dims[0]):
    for x in range(x_half+1, dims[1]):
        q4 += counter[(y,x)]

res = q1*q2*q3*q4
print(res)

"""PART 2"""
# visualize tree
def visualize_tree(positions):
    grid = [[0 for i in range(dims[1])] for j in range(dims[0])]
    for y,x in positions.values():
        grid[y][x] = 1

    for line in grid:
        print(line)

# reinitialize robots
positions = {}
velocities = {}
for idx, line in enumerate(lines):
    robot_regex = re.compile(r"p=(.?\d+),(.?\d+) v=(.?\d+),(.?\d+)")
    robot = re.match(robot_regex, line)

    p = int(robot.group(2)), int(robot.group(1))
    v = int(robot.group(4)), int(robot.group(3))

    positions[idx] = p
    velocities[idx] = v

res = 93
positions = move(positions, 93)
while True:
    input()
    print('#'*20, res, '#'*20)
    print('\n'*5)
    visualize_tree(positions)

    positions = move(positions, 101)
    res += 101