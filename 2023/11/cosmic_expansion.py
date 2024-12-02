import numpy as np

def main():

    path = './input.txt'
    # path = './sample_input.txt'
    # path = './sample_input2.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = cosmic_expansion(lines, expansion_rate = 2)
        res2 = cosmic_expansion(lines, expansion_rate = 1000000)

    return res1, res2

def cosmic_expansion(lines, expansion_rate):

    expanded_rows, expanded_cols = expand_space(lines)

    galaxies = find_galaxies(lines)

    distance = 0

    for i in range(len(galaxies)):

        for j in range(i+1, len(galaxies)):

            distance += manhattan_distance(i, j, galaxies, expanded_rows, expanded_cols, expansion_rate)

    return distance

def expand_space(lines):
    empty_cols = [True]*len(lines[0])
    empty_rows = [True]*len(lines)

    for r, row in enumerate(lines):

        for c, val in enumerate(row): 

            if val == '.': continue

            empty_cols[c] = False
            empty_rows[r] = False

    return [i for i, r in enumerate(empty_rows) if r], [i for i, c in enumerate(empty_cols) if c]

def find_galaxies(lines):

    galaxies = []

    for r, row in enumerate(lines):

        for c, val in enumerate(row):

            if val == '#':

                galaxies.append((r,c))

    return galaxies

def manhattan_distance(g1, g2, galaxies, expanded_rows, expanded_cols, expansion_rate):

    r1, c1 = galaxies[g1]
    r2, c2 = galaxies[g2]

    dist = abs(r2-r1) + abs(c2-c1)

    for r in expanded_rows:

        if r1 <= r <= r2 or r2 <= r <= r1:

            dist += expansion_rate - 1

    for c in expanded_cols:

        if c1 <= c <= c2 or c2 <= c <= c1:

            dist += expansion_rate - 1

    return dist


if __name__ == '__main__':

    print(main())