import re

import sys
sys.path.append('../')
from functions import read_file, print_answers


def calculate_all_product_sums(text):
    res = 0

    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text):
         
        """REGEX
        mul: find all instances of "mul"
            \(: find "("
            \): find "("
            \d{1,3}: special string of digits with length 1-3 => (...) captures a unique group instance to match
        """

        x1, x2 = match.group(1), match.group(2)

        res += int(x1)*int(x2)

    return res

def calculate_all_enabled_product_sums(text):
    last = True
    res = 0
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", text):
        
        """REGEX
        mul: find all instances of "mul"
            \(: find "("
            \): find "("
            \d{1,3}: special string of digits with length 1-3 => (...) captures a unique group instance to match
        OR
        do\(\): all instances of "do()"
        OR
        don't\(\): all instances of "don't()"
        """

        if match.group(0) == "do()":
            last = True
        elif match.group(0) == "don't()":
            last = False
        elif last:
                x1, x2 = match.group(1), match.group(2)
                res += int(x1)*int(x2)

    return res

def main(path):
    text = read_file(path)

    ans1 = calculate_all_product_sums(text)
    ans2 = calculate_all_enabled_product_sums(text)

    print_answers(path, ans1, ans2)

main('3/sample_input.txt')
main('3/input.txt')

"""
def get_product_sum(text):
    muls = text.split('mul(') # split text into array of substrings, each with one instace of "mul("
    prod_sum = 0
    for mul in muls[1:]:

        x1 = None
        x2 = None
        
        switch = False
        idx = 0
        curr = ''

        while idx < len(mul):
            if mul[idx].isnumeric(): # ensure that mul operation is not corrupted
                curr += mul[idx]
            elif mul[idx] == ',': # switch over to search for RHS number
                if not switch:
                    x1 = int(curr)
                    curr = ''
                    switch = True
            elif mul[idx] == ')' and switch: # end search
                x2 = int(curr)
                prod_sum += x1*x2
                break
            else:
                break
            idx += 1

    return prod_sum

def calculate_all_enabled_product_sums(text):
    enabled_texts = []
    low = 0
    first = True

    while low < len(text):
        do_idx = low + text[low:].index("do()") if "do()" in text[low:] else len(text) # find earliest index of "do"
        dont_idx = low + text[low:].index("don't()") if "don't()" in text[low:] else len(text) # find earliest index of "don't()"

        if first: # if this is iteration, then it is part of do()
            enabled_texts.append((low, dont_idx))
            first = False
            low = dont_idx
        else:
            if do_idx < dont_idx: # assumes that current substring is in dont() state
                enabled_texts.append((do_idx, dont_idx)) # skip to earliest do() and add substring until next dont()
                low = dont_idx # go to next instance of don't()
            else:
                low = do_idx # go to next instace of do()
    
    prod_sum = 0
    for low, high in enabled_texts:
        prod_sum += get_product_sum(text[low:high])

    return prod_sum

def calculate_all_product_sums(text):
 
    res = get_product_sum(text)

    return res

def main(path):

    with open(path, 'r') as f:
        text = f.read()

    ans1 = calculate_all_product_sums(text)
    print()
    ans2 = calculate_all_enabled_product_sums(text)

    print_answers(path, ans1, ans2)

main('3/sample_input.txt')
main('3/input.txt')
"""