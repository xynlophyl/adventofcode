from collections import defaultdict

path = '8/sample_input.txt'
path = '8/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()
# print(len(lines), len(lines[0]))

"""PART 1"""
def find_antennas(lines):
    antennas = defaultdict(list)

    for r, row in enumerate(lines):
        for c, val in enumerate(row):
            if val != '.':
                antennas[val].append((r,c))

    return antennas

dirs = [(1,1), (-1,-1)]
def get_possible_anti_antennas(locations):

    def check_possible_anti_antenna(anti, other):
        # print(anti)
        anti_r, anti_c = anti
        r, c = other
        if (anti_r, anti_c) == (r,c): # found the other antenna
            # print('found pair')
            return False
        elif anti_r < 0 or anti_r >= len(lines) or anti_c < 0 or anti_c >= len(lines[0]): # anti antenna outside grid
            # print('outside grid')
            return False
        else:
            return True
    
    for idx, (r1,c1) in enumerate(locations):
        for (r2, c2) in locations[idx+1:]:
            #  calculate distance between two resonating antennas
            dist_r, dist_c = r1-r2, c1-c2
            anti_r, anti_c = r1+dist_r*1, c1+dist_c*1
            if check_possible_anti_antenna((anti_r, anti_c), (r2, c2)):
                # print(anti_r, anti_c)
                # print(lines[anti_r][anti_c])
                anti_antennas.add((anti_r, anti_c))
            anti_r, anti_c = r2+dist_r*-1, c2+dist_c*-1
            if check_possible_anti_antenna((anti_r, anti_c), (r1,c1)):
                anti_antennas.add((anti_r, anti_c))

antennas = find_antennas(lines)

anti_antennas = set()
for antenna, locations in antennas.items():
    get_possible_anti_antennas(locations)

res = len(anti_antennas)
print(res)

"""PART 2"""
def get_possible_anti_antennas(locations):
        
    for idx, (r1,c1) in enumerate(locations):
        for (r2, c2) in locations[idx+1:]:
            #  calculate distance between two resonating antennas
            dist_r, dist_c = r1-r2, c1-c2
            multiplier = 1
            while True:
                anti_r, anti_c = r2+dist_r*multiplier, c2+dist_c*multiplier
                if anti_r < 0 or anti_r >= len(lines) or anti_c < 0 or anti_c >= len(lines[0]): # anti antenna outside grid
                    # print('outside grid')
                    break
                else:
                    anti_antennas.add((anti_r, anti_c))

                multiplier += 1
        
            multiplier = -1
            while True:
                anti_r, anti_c = r1+dist_r*multiplier, c1+dist_c*multiplier
                if anti_r < 0 or anti_r >= len(lines) or anti_c < 0 or anti_c >= len(lines[0]): # anti antenna outside grid
                    # print('outside grid')
                    break
                else:
                    anti_antennas.add((anti_r, anti_c))
                multiplier  -= 1

anti_antennas = set()
for antenna, locations in antennas.items():
    get_possible_anti_antennas(locations)
res = len(anti_antennas)
print(res)

""""""
def visualize_anti_antennas(anti_antennas):
    tmp = lines
    for (r,c) in anti_antennas:
        tmp[r] = tmp[r][:c] + '#' + tmp[r][c+1:]
    for line in tmp:
        print(line)

# visualize_anti_antennas(anti_antennas)