import sys
sys.path.append('../')
from functions import read_file, print_answers

def parse_inputs(text):
    lines = text.splitlines()

    parsed_lines = []

    for line in lines:

        line = line.strip()
        
        parsed_line = [int(x) for x in line.split(' ')]

        parsed_lines.append(parsed_line)
    
    return parsed_lines

def check_safety(lines):
    count = 0

    for line in lines:
        low, high = 0, len(line) - 1 # two pointer, work from edges to middle

        ord_flag = (line[0] - line[low+1]) > 0

        while low < high:

            low_diff = line[low] - line[low+1]
            high_diff = line[high-1] - line[high]

            low_adj_flag = 0 < abs(low_diff) < 4
            high_adj_flag = 0 < abs(high_diff) < 4

            if not(low_adj_flag and high_adj_flag and ord_flag == (low_diff > 0) and ord_flag == (high_diff > 0)): # requirements not satisfied
                break

            low += 1
            high -= 1
        else:
            count += 1

    return count


def check_safety_with_dampener(lines):
    
    def check(line, idx): 
        if idx != -1:
            new_line = line[:idx] + line[idx+1:] 
        else:
            new_line = line[:]

        ords = [new_line[i] > new_line[i+1] for i in range(len(new_line)-1)]
        adjs = [0 < abs(new_line[i+1] - new_line[i]) < 4 for i in range(len(new_line) -1)]

        return sum(ords) in [0, len(new_line) - 1] and sum(adjs) == len(new_line) - 1
    
    count = 0
    for line in lines:
        for idx in range(-1, len(line), 1): # brute force: try every possible combination of dampening (and no dampening)
            if check(line, idx):
                count += 1
                break
    
    return count

def main(path):

    text = read_file(path)

    lines = parse_inputs(text)

    ans1 = check_safety(lines)
    ans2 = check_safety_with_dampener(lines)
    
    print_answers(path, ans1, ans2)

main('2/sample_input.txt')
main('2/input.txt')
