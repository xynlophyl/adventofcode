from collections import deque

def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
    
    res1 = add_scores(lines)
    res2 = count_scratches(lines)

    return res1, res2

def add_scores(lines):

    score = 0

    for l in lines:

        score += calculate_card(l)

    return score

def calculate_card(line):

    _, numbers = line.split(':')

    winning_nums, lottery_nums = numbers.split('|')

    winning_nums = set(winning_nums[1:].split(' '))

    count = 0 
    for lot in lottery_nums[1:].split(' '):

        if lot != '' and lot in winning_nums:

            count += 1

    if count:
        return 2**(count-1)
    return 0

def count_scratches(lines):

    won_cards = {i: [] for i in range(len(lines))}
    
    for i, l in enumerate(lines):

        won_cards[i] = find_next_winners(l, i)

    card_counts = {i: 1 for i in range(len(lines))}

    for card, next_cards in won_cards.items():

        for nc in next_cards:

            card_counts[nc] += card_counts[card]

    return sum(card_counts.values())



def find_next_winners(line, curr_card):

    _, numbers = line.split(':')

    winning_nums, lottery_nums = numbers.split('|')

    winning_nums = set(winning_nums[1:].split(' '))

    count = 0 
    for lot in lottery_nums[1:].split(' '):

        if lot != '' and lot in winning_nums:

            count += 1

    return [curr_card + c + 1 for c in range(count)]

if __name__ == '__main__':

    print(main())


