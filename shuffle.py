# shuffle four kinds of colour of card each containing 1 to 13 numbers

import random

suits = ['heart', 'spade', 'diamond', 'club']
ranks = range(1,14)


deck = [(suit, rank) for rank in ranks for suit in suits]

random.shuffle(deck)


for i in range(5):
    print(f"{deck[i][0]} of {deck[i][1]}")