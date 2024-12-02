from tqdm import tqdm

def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
    
    res1 = seed_fertilizer(lines)
    res2 = seed_fertilizer2(lines)

    return res1, res2

def seed_fertilizer(lines):
    # takes an array of lines that perform: maps an array of seed values and finds the minimum final value

    seeds = lines[0].split(':')[1][1:].split(' ')
    map = {int(s): int(s) for s in seeds}

    # for i, line in tqdm(enumerate(lines[1:])):
    i = 0
    while i < len(lines):

        line = lines[i]

        if line and line[0].isnumeric():

            map, i = create_map(lines, i, map)

        i += 1
    
    # print(map)
    return min(map.values())

def create_map(lines, idx, map):

    # print(lines[idx-1])
    # start = idx

    while idx < len(lines) and lines[idx]:

        dest, src, rng = lines[idx].split(' ')
        dest, src, rng = int(dest), int(src), int(rng)

        for s, val in map.items():

            # if initial seed value is in the range of the map's source range -> map to its corr. value in destination range
            if src <= s and s < src+rng:

                map[s] = val - src + dest

        idx += 1

    # print(start+1, idx+1)
    
    return {val: val for val in map.values()}, idx

def seed_fertilizer2(lines):
    # takes an array of lines that perform: maps (seed_start, range) pairs (not in tuple form) given a series of mapping requirements  and finds the smallest final value

    seeds = lines[0].split(':')[1][1:].split(' ')
    seeds = parse_seed_ranges(seeds)
    
    map = {s: s for s in seeds}

    # for i, line in tqdm(enumerate(lines[1:])):
    i = 0
    while i < len(lines):

        line = lines[i]

        if line and line[0].isnumeric():

            map, i = create_map2(lines, i, map)
            map = parse_new_map(map)

        i += 1
    
    return get_min_value(map)

def parse_seed_ranges(seeds):
    # creates array tuples of lower_bound, upper_bound, given lower_bound and range

    new_seeds = []

    for i in range(0, len(seeds), 2):

        start = int(seeds[i])
        rng = int(seeds[i+1])
        new_seeds.append((start, start+rng-1))
    
    return new_seeds

def create_map2(lines, idx, map):
    # iterates through each line of mappings and maps relevant values to their corresponding values

    print(lines[idx-1])

    new_map = {}
    map_changes = {}

    while idx < len(lines) and lines[idx]:

        dest, src, rng = lines[idx].split(' ')
        dest, src, rng = int(dest), int(src), int(rng)

        # defining range of source values for mapping
        src_low, src_high = src, src + rng -1

        for low, high in map:

            if (low, high) in new_map: continue

            elif src_low > high or src_high < low: continue

            elif src_low <= low and src_high >= high: 
                # if current range is bounded within the mapping range -> all values in current range are mapped to new values (1 range)
                
                new_map[(low,high)] = [(low - src + dest, high - src + dest)]

            elif src_low > low and src_high < high: 
                # if current range completely bounds the mapping range -> only values in mapping range are mapped and new ranges are created for non-mapped values (3 ranges)

                new_map[(low,high)] = [(dest, dest + rng)]
                map_changes[(low, src_low-1)] = [(low, src_low-1)]
                map_changes[(src_high+1, high)] = [(src_high+1, high)] 

            elif src_low > low and src_high >= high: 
                # if only lower end of current range is NOT included in mapping -> lower unmapped range AND upper mapped range (2 ranges)
        
                new_map[(low, high)] = [(dest, high - src + dest)]
                map_changes[(low, src_low-1)] = [(low, src_low-1)]
            
            elif src_low <= low and src_high < high: 
                # if only upper end of current range is NOT included in mapping -> lower mapped range AND upper unmapped range (2 ranges)

                new_map[(low, high)] = [(low - src_low + dest, dest + rng)]
                map_changes[(src_high+1, high)] = [(src_high+1, high)]
        
        # updating map key ranges to take in ranges that were unmapped and sliced from its original range   
        map = map | map_changes 
         
        idx += 1


    for i in map:

        if i not in new_map:

            new_map[i] = [i]

    # print(new_map)

    return new_map, idx

def parse_new_map(map):
    # recreates mapping hash table for next section of mapping rules (takes previous hash table values and splits them into individual (low, high) tuples to use as keys, which map to themselves)

    new_map = {}

    print(map)

    for old_range, new_ranges in map.items():

        # print(new_ranges)

        for r in new_ranges:

            new_map[r] = r

    # print(new_map)
    return new_map

def get_min_value(map):
    # finds the smallset final value

    # print('FINAL', list(map.keys()))

    min_val = float('inf')

    for low, high in map:

        min_val = min(min_val, low, high)

    return min_val



if __name__ == '__main__':

    print(main())
        
