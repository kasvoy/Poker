"""
Takes in a list of cards and an argument corresponding to the hand we're looking for
if there is a pair (number == 2) - returns the number of pairs in the list
if there is a 3 of a kind (number == 3) or 4 of a kind (number == 4) returns True
"""
def is_pair_three_four(cards, number):

    ranks = [card.rank for card in cards]
    
    pair_ranks = {rank for rank in ranks if ranks.count(rank) == number}

    if number == 2:
        return len(pair_ranks)

    if len(pair_ranks) >= 1:
        return True
    
    return False

def is_flush(cards):

    suits = {card.suit for card in cards}
    if len(suits) == 1:
        return True
    return False

def is_straight(cards):

    sorted_ranks = sorted([int(card) for card in cards])

    seq = [i for i in range(min(sorted_ranks), max(sorted_ranks) + 1)]

    if sorted_ranks == seq:
        return True
    
    #when Ace counts as "One"
    elif (14 in sorted_ranks):
        sorted_ranks.remove(14)
        sorted_ranks.append(1)
        newsorted = sorted(sorted_ranks)

        if newsorted == [i for i in range(min(newsorted), max(newsorted) + 1)]:
            return True

    return False
    
def is_fullhouse(cards):
    if (is_pair_three_four(cards, 2) == 1 and is_pair_three_four(cards, 3)):
        return True
    
    return False

"""
Takes a 5 card list and returns a hand identifier as below:

0 - Highcard
1 - Pair
2 - Two Pairs
3 - Three of a kind
4 - Straight
5 - Flush
6 - Full House
7 - Four of a kind
8 - Straight flush

"""
def identify_hand(cards):
    
    if is_straight(cards) and is_flush(cards):
        return 8

    if is_pair_three_four(cards, 4):
        return 7
    
    if is_fullhouse(cards):
        return 6
    
    if is_flush(cards):
        return 5
    
    if is_straight(cards):
        return 4
    
    if is_pair_three_four(cards, 3):
        return 3
    
    if is_pair_three_four(cards, 2) == 2:
        return 2

    if is_pair_three_four(cards, 2) == 1:
        return 1

    else:
        return 0
