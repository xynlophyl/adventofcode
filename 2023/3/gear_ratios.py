def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
    
    res1 = gear_ratios(lines)
    res2 = gear_ratios2(lines)

    return res1, res2

def gear_ratios(lines):

    numbers = {}

    for r, line in enumerate(lines):

        for c, val in enumerate(line):

            if not (val.isnumeric() or val == '.'):

                numbers = numbers | find_adj_numbers(lines, r, c)

    return sum(numbers.values())

def gear_ratios2(lines):

    res = 0

    for r, line in enumerate(lines):

        for c, val in enumerate(line):

            if not (val.isnumeric() or val == '.'):

                adj_nums = find_adj_numbers(lines, r, c)

                if len(adj_nums) == 2:

                    res += dict_product(adj_nums)

    return res

def dict_product(d):

    prod = 1

    for i in d.values():

        prod *= i
    
    return prod

def find_adj_numbers(lines, r, c):

    dirs = [(-1,0), (-1,-1), (-1,1), (0, -1), (0,1), (1,0), (1,-1), (1,1)]

    numbers = {}

    for dx, dy in dirs:

        new_r, new_c = r+dx, c+dy

        if lines[new_r][new_c].isnumeric():

            curr_line = lines[new_r]

            m = len(curr_line)

            low = high = new_c

            while low >= 0 and high < m:

                if not (curr_line[low].isnumeric() or curr_line[high].isnumeric()):

                    break

                if curr_line[low].isnumeric():

                    low -= 1

                if curr_line[high].isnumeric():

                    high += 1

            numbers[(new_r, low+1)] = int(curr_line[low+1:high])
                
    return numbers


if __name__ == '__main__':

    print(main())
