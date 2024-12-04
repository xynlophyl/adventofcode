import heapq

import sys
sys.path.append('../')
from functions import read_file, print_answers

def parse_input(text):

    lines = text.splitlines()

    col1, col2 = [], []

    for line in lines:

        line = line.strip()

        x1, x2 = line.split('   ')
        col1.append(int(x1))
        col2.append(int(x2))

    return col1, col2

def sum_difference_in_min_pairs(col1, col2):

    col1 = col1[:]
    col2 = col2[:]

    # create heap
    heapq.heapify(col1)
    heapq.heapify(col2)

    res = 0

    while len(col1) > 0:
        
        # pop from both heaps
        x1 = heapq.heappop(col1)
        x2 = heapq.heappop(col2)

        # calculate sum of absolute differences 
        res += abs(x1-x2)

    return res

def calculate_similarity_score(col1, col2):

    counts = {}

    # count occurrences
    for i in col2:
        counts[i] = counts.get(i, 0) + 1
    
    res = 0
    # calculate similarity
    for i in col1:
        res += i*counts.get(i, 0)

    return res

def main(path):

    text = read_file(path)

    # separate into two separate lists
    col1, col2 = parse_input(text)

    assert len(col1) == len(col2)

    # q1
    ans1 = sum_difference_in_min_pairs(col1, col2)

    # q2
    ans2 = calculate_similarity_score(col1, col2)

    print_answers(path, ans1, ans2)


main('1/sample_input.txt')
main('1/input.txt')