import deck

# NOTE: This encoder only uses capital letters!
# The input should be capitalized, and the program will capitalize it anyways
# if it isn't. The output will also be capitalized. This includes the key as well.abs

def key_as_deck(key):
    key = key.capitalize()
    deck = card.get_deck()
    

# Generation of the keystream using the deck of cards

def keystream_gen(key):
    # The deck of cards, as an alphanumerical representation.
    # NOTE: This deck includes the Jokers, which is important for the keystream generation.
    deck = [str(card) for card in range(1, 52 + 1)] + ["A", "B"]
    # Bridge suits order is spades, hearts, diamonds, clubs

    print(deck)
