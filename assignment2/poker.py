#!/usr/bin/env python

import random

class Card(object):
    """ represents a standard playing card. """
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None,"Ace", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "Jack", "Queen", "King"]

    def __repr__(self):
        return "%s of %s" % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(Card):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def top_card(self):
        return self.cards[0]

    def add_card(self, card):
        self.cards.append(card) 

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        __cmp__.sort(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
   
    def deal_hand(self, card_num):
        hand1 = []
        while len(hand1) < card_num:
            card1 = self.pop_card()
            hand1.append(card1)
        return hand1

    def deal_game(self, player_num, card_num):
        game1 = []
        while len(game1) < player_num:
            hand1 = self.deal_hand(card_num)
            game1.append(hand1)
        return game1

if __name__ == "__main__":
    
    deck = Deck()
    deck.shuffle()
    game = deck.deal_game(3, 5)
    print(game)






