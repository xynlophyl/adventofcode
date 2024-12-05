from collections import defaultdict, deque

import sys
sys.path.append('../')
from functions import read_file, print_answers

def parse_text(text):
    lines = text.splitlines()
    
    rules = []

    for idx, line in enumerate(lines):
        if line == '':
            break
        else:
            rules.append(line)

    orders = lines[idx+1:]

    return rules, orders

def get_links(rules):
    """generate mapping of each element to its required predecessors"""

    links = defaultdict(list)

    for line in rules:

        prev, nxt = line.split('|')

        links[nxt].append(prev)

    return links

def reorder(order, links):
    queue = deque(order)
    new_order = []

    while queue:

        curr = queue.popleft()

        for y in links[curr]: # gets all elements that curr needs
            if y in order: # checks that y is in order (first requirement)
                if y in new_order: # checks that y is also satisfied in new order (second requirement)
                    continue
                else:
                    queue.append(curr) # send to back of queue for later processing
                    break
        else:
            new_order.append(curr) # if all of curr's required predecessors are satisfied, then add it to the new order

    return new_order
        
def reorder_then_sum(orders, links):
    res = 0

    for order in orders:

        new_order = reorder(order, links)
    
        res += int(new_order[len(new_order)//2])

    return res

def check_order(order, links):
    visited = set()
    flag = True
    for x in order:
        for y in links[x]: # get all x's required predecessors
            if y in order and y not in visited: # if y in order, but isn't before x, then requirements failed
                flag = False
                break
        
        if not flag:
            break
        visited.add(x)

    return flag

def get_sum_of_middle(orders, links):
    bad_orders = []

    res = 0
    for line in orders:

        order = line.split(',')

        if check_order(order, links):
            res += int(order[len(order)//2])
        else:
            bad_orders.append(order)

    return res, bad_orders

def main(path):
    text = read_file(path)

    rules, orders = parse_text(text)

    links = get_links(rules)

    ans1, bad_orders = get_sum_of_middle(orders, links)

    ans2 = reorder_then_sum(bad_orders, links)

    print_answers(path, ans1, ans2)

main('5/sample_input.txt')
main('5/input.txt')
