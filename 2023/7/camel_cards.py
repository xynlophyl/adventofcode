import numpy as np

def main():

    path = './input.txt'
    # path = './sample_input.txt'
    # path = './sample_input2.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = camel_cards(lines)
        res2 = camel_cards2(lines)

    return res1, res2

def camel_cards(lines):

    hands = []
    hand_strengths = []
    bids = []

    for l in lines:

        hand, bid = l.split(' ')

        strength = parse_hand(hand)

        hands.append(hand)
        hand_strengths.append(strength)
        bids.append(int(bid))

    hand_strengths = np.array(hand_strengths, dtype = 'i,i,i,i,i,i')
    hands = np.array(hands)
    bids = np.array(bids)

    # print(hands[0], hand_strengths[0])

    ranks = np.argsort(hand_strengths)

    # print(ranks)
    # print(bids)
    # print('bids*rank', bids*(ranks+1))

    return np.sum(bids[ranks]*[i+1 for i in range(bids.shape[0])]) 

def parse_hand(hand):

    cards = [str(i+2) for i in range(8)] + ['T', 'J', 'Q', 'K', 'A']

    card_ranks = {
        i: idx for idx, i in enumerate(cards)
    }

    card_counts = {
        i+1: 0 for i in range(5)
    }

    card_num =[card_ranks[c] for c in hand]

    explored = set()

    for card in hand:

        if card in explored: continue

        explored.add(card)

        card_counts[hand.count(card)] += 1
    
    if card_counts[5] ==1:

        rank = 0
    
    elif card_counts[4] == 1:

        rank =  1
    
    elif card_counts[3] == 1 and card_counts[2] == 1:

        rank = 2
    
    elif card_counts[3] == 1:

        rank = 3
    
    elif card_counts[2] == 2:

        rank = 4
    
    elif card_counts[2] == 1:

        rank = 5
    
    else:
        rank = 6

    return tuple([-rank] + card_num)
    
def camel_cards2(lines):

    hands = []
    hand_strengths = []
    bids = []

    for l in lines:

        hand, bid = l.split(' ')

        strength = parse_hand2(hand)

        hands.append(hand)
        hand_strengths.append(strength)
        bids.append(int(bid))

    hand_strengths = np.array(hand_strengths, dtype = 'i,i,i,i,i,i')
    hands = np.array(hands)
    bids = np.array(bids)

    # print(hands[0], hand_strengths[0])

    ranks = np.argsort(hand_strengths)

    # print(hands)
    # print(hand_strengths)
    # print(hands[ranks])
    # print(bids[ranks])
    # print('bids*rank', bids*(ranks+1))

    return np.sum(bids[ranks]*[i+1 for i in range(bids.shape[0])]) 

def parse_hand2(hand):

    cards = ['J'] + [str(i+2) for i in range(8)] + ['T', 'Q', 'K', 'A']

    card_ranks = {
        i: idx for idx, i in enumerate(cards)
    }

    card_num =[card_ranks[c] for c in hand]


    card_counts = {
        i+1: 0 for i in range(5)
    }

    J_count = hand.count('J')

    explored = set('J')

    for card in hand:

        if card in explored: continue
        
        explored.add(card)
        card_counts[hand.count(card)] += 1
    
    if card_counts[5] or J_count == 5 or J_count == 4 or (J_count == 1 and card_counts[4]) or (J_count == 2 and card_counts[3]) or (J_count == 3 and card_counts[2]): 
        # five of a kind
        rank = 0

    elif card_counts[4] or J_count == 3 or (J_count == 1 and card_counts[3]) or (J_count == 2 and card_counts[2]): 
        # four of a kind
        rank = 1

    elif (card_counts[3] and card_counts[2]) or (J_count == 2 and card_counts[3]) or (J_count == 3 and card_counts[2]) or (card_counts[2] == 2 and J_count == 1): 
        # full house
        rank = 2

    elif (card_counts[3]) or J_count == 2 or (J_count == 1 and card_counts[2]):
        # triple

        rank = 3
    
    elif (card_counts[2] == 2) or (J_count == 1 and card_counts[2] == 1):
        # two pair
        rank = 4
    
    elif (card_counts[2]) or J_count == 1: 
        # pair
        rank = 5

    else: 
        # high card
        rank = 6

    return tuple([-rank] + card_num)

if __name__ == '__main__':

    print(main())