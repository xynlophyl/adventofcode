import sys
sys.path.append('../')
from functions import read_file, print_answers

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