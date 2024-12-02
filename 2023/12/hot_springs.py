from functools import cache

def hot_springs(lines):

    res = 0
    
    for l in lines:

        res += parse_record(l)

    return res

def parse_record(record):

    springs, groups = record.split(' ')
    groups = tuple(groups.split(','))

    return get_combinations(springs, groups, 0)
    # return get_combinations_vis(springs, groups, 0, springs[:])

@cache
def get_combinations(springs, groups, count):

    # print(springs, len(springs), len(groups), count)
    # print(springs_filled)
    # print()

    if len(springs) == 0:

        if len(groups) == 0 or (len(groups) == 1 and count == int(groups[0])):

            return 1
        
        else:
        
            return 0

    elif groups and count > int(groups[0]):

        return 0

    curr = springs[0]

    if curr == '.':

        if count != 0:

            if count == int(groups[0]):

                return get_combinations(springs[1:], groups[1:], 0)
            
            else: 

                return 0

        return get_combinations(springs[1:], groups, 0)

    elif curr == '#':

        if len(groups) == 0:

            return 0

        return get_combinations(springs[1:], groups, count+1)

    elif curr == '?':

        if len(groups) == 0:

            return get_combinations(springs[1:], groups, count)

        elif count == 0:

            return get_combinations(springs[1:], groups, 0) + get_combinations(springs[1:], groups, 1)

        elif count == int(groups[0]):

            return get_combinations(springs[1:], groups[1:], 0)

        elif count < int(groups[0]):

            return get_combinations(springs[1:], groups, count+1)

@cache
def get_combinations_vis(springs, groups, count, springs_filled):

    # print(springs, len(springs), len(groups), count)
    # print(springs_filled)
    # print()

    if len(springs) == 0:

        if len(groups) == 0 or (len(groups) == 1 and count == int(groups[0])):

            print(springs_filled)

            return 1
        
        else:
        
            return 0

    elif groups and count > int(groups[0]):

        return 0

    curr = springs[0]

    if curr == '.':

        if count != 0:

            if count == int(groups[0]):

                return get_combinations_vis(springs[1:], groups[1:], 0, springs_filled[:])
            
            else: 

                return 0

        return get_combinations_vis(springs[1:], groups, 0, springs_filled[:])

    elif curr == '#':

        if len(groups) == 0:

            return 0

        return get_combinations_vis(springs[1:], groups, count+1, springs_filled[:])

    elif curr == '?':

        if len(groups) == 0:

            foo = springs_filled[:len(springs_filled)-len(springs)] + '.' + springs_filled[len(springs_filled)-len(springs)+1:]

            return get_combinations_vis(springs[1:], groups, count, foo)

        elif count == 0:

            foo1 = springs_filled[:len(springs_filled)-len(springs)] + '.' + springs_filled[len(springs_filled)-len(springs)+1:]
            foo2 = springs_filled[:len(springs_filled)-len(springs)] + '#' + springs_filled[len(springs_filled)-len(springs)+1:]

            return get_combinations_vis(springs[1:], groups, 0, foo1) + get_combinations_vis(springs[1:], groups, 1, foo2)

        elif count == int(groups[0]):

            foo = springs_filled[:len(springs_filled)-len(springs)] + '.' + springs_filled[len(springs_filled)-len(springs)+1:]

            return get_combinations_vis(springs[1:], groups[1:], 0, foo)

        elif count < int(groups[0]):

            foo = springs_filled[:len(springs_filled)-len(springs)] + '#' + springs_filled[len(springs_filled)-len(springs)+1:]

            return get_combinations_vis(springs[1:], groups, count+1, foo)
        
def hot_springs2(lines):

    res = 0

    for l in lines:

        res += parse_record2(l)

    return res

def parse_record2(record):

    springs, groups = record.split(' ')
    groups = tuple(groups.split(','))

    return get_combinations(((springs+'?')*5)[:-1], groups*5, 0)

def main():

    path = './input.txt'
    # path = './sample_input.txt'
    # path = './sample_input2.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = hot_springs(lines)
        res2 = hot_springs2(lines)
        # res2 = None

    return res1, res2

if __name__ == '__main__':

    print(main())