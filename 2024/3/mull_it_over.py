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

    with open(path, 'r') as f:
        text = f.read()

    ans1 = calculate_all_product_sums(text)
    ans2 = calculate_all_enabled_product_sums(text)

    print_answers(path, ans1, ans2)

main('3/sample_input.txt')
main('3/input.txt')

"""
def get_product_sum(text):

    muls = text.split('mul(')
    prod_sum = 0
    for mul in muls[1:]:

        x1 = None
        x2 = None
        
        switch = False
        idx = 0
        curr = ''

        while idx < len(mul):
            if mul[idx].isnumeric():
                curr += mul[idx]
            elif mul[idx] == ',':
                if not switch:
                    x1 = int(curr)
                    curr = ''
                    switch = True
            elif mul[idx] == ')' and switch:
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

        do_idx = low + text[low:].index("do()") if "do()" in text[low:] else len(text)
        dont_idx = low + text[low:].index("don't()") if "don't()" in text[low:] else len(text)

        if first:
            enabled_texts.append((low, dont_idx))
            first = False
            low = dont_idx
        else:
            if do_idx < dont_idx:
                enabled_texts.append((do_idx, dont_idx))
                low = dont_idx
            else:
                low = do_idx
                first 
    
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