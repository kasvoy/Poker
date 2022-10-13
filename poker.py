import random

ids = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
        "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]




class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return self.rank + self.suit
    
    def __int__(self):
        if self.rank == "J":
            return 11
        elif self.rank == "Q":
            return 12
        elif self.rank == "K":
            return 13
        elif self.rank == "A":
            return 14
        else:
            return int(self.rank)
            


class Player:
    def __init__(self):
        self.no_chips = 100
        self.hole_cards = []
        self.isDealer = False
        
    def show_cards(self):
        for card in self.hole_cards:
            print(card)

        
class PokerTable:
    
    def __init__(self, no_players):
        self.community_cards = []
        self.players = []
        self.deck = []
        self.no_bet_rounds = 0
        self.bb = 2
        self.pot = 0
        

        #initialize a standard 52 card deck as a list of Card objects    
        for id in ids:
            if len(id) == 3:
                self.deck.append(Card("10", id[2]))
            else:
                self.deck.append(Card(id[0], id[1]))    
        
        #set a list of players
        for i in range(no_players):
            self.players.append(Player())

        self.players_in = self.players.copy()
        
        self.players[0].isDealer = True
        
        #shuffle the deck
        random.shuffle(self.deck)
    
    #deal 2 cards to each of the players
    def deal_cards(self):            
        for player in self.players:
            while len(player.hole_cards) < 2:
                player.hole_cards.append(self.deck.pop(0))
                    
    
    def print_player_cards(self):
        i = 1
        for player in self.players:
            print("Player " + str(i) + " cards:")
            player.show_cards()
            i+=1
            print("\n")
    
    def print_community_cards(self):
        
        for card in self.community_cards:
            print(card)
        
        print("\n")
        
        
    def add_community_card(self):
        
        #Flop
        if self.no_bet_rounds == 0:
            while len(self.community_cards) < 3:
                self.community_cards.append(self.deck.pop(0))
        
        #Turn / River   
        else:
            self.community_cards.append(self.deck.pop(0))
        
        self.no_bet_rounds += 1   
    
        
        
    def print_deck(self):
        for card in self.deck:
            print(card)
        print("\n")

    def bet(self, player, amount):
        player.no_chips -= amount
        self.pot += amount
    
    def fold(self, player):
        self.players_in.remove(player)


"""
#Takes in a list of cards and an argument corresponding to the hand we're looking for
#if there is a pair (number == 2) - returns the number of pairs in the list
#if there is a 3 of a kind (number == 3) or 4 of a kind (number == 4) returns True

"""
def identify_pair_three_four(cards, number):

    ranks = [card.rank for card in cards]
    
    pair_ranks = {rank for rank in ranks if ranks.count(rank) == number}

    if number == 2:
        return len(pair_ranks)

    if len(pair_ranks) >= 1:
        return True
    
    return False

def identify_flush(cards):

    suits = {card.suit for card in cards}
    if len(suits) == 1:
        return True
    return False

def identify_straight(cards):

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

def identify_fullhouse(cards):
    if (identify_pair_three_four(cards, 2) == 1 and identify_pair_three_four(cards, 3)):
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
    
    if identify_straight(cards) and identify_flush(cards):
        return 8

    if identify_pair_three_four(cards, 4):
        return 7
    
    if identify_fullhouse(cards):
        return 6
    
    if identify_flush(cards):
        return 5
    
    if identify_straight(cards):
        return 4
    
    if identify_pair_three_four(cards, 3):
        return 3
    
    if identify_pair_three_four(cards, 2) == 2:
        return 2

    if identify_pair_three_four(cards, 2) == 1:
        return 1

    else:
        return 0



