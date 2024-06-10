JOKER_A = "A"
JOKER_B = "B"

# Bridge suits order is
# Clubs     (+0),
# Diamonds (+13),
# Hearts   (+26),
# Spade    (+39),
# Jokers    (53).

def get_fixed_deck():
    return [str(card) for card in range(1, 52 + 1)] + ["A", "B"]

def move_a_joker(deck):
    joker_index = deck.index(JOKER_A)
    
    # If the joker is the bottom card of the deck, move it just below the top card
    if joker_index == len(deck) - 1:
        deck.remove(JOKER_A)
        deck.insert(1, JOKER_A)
    # Otherwise, move the joker one card down
    else:
        deck.remove(JOKER_A)
        deck.insert(joker_index + 1, JOKER_A)

    return deck


def move_b_joker(deck):
    joker_index = deck.index(JOKER_B)

    # If the joker is the bottom card of the deck, move it just below
    # the second card.
    if joker_index == len(deck) - 1:
        deck.remove(JOKER_B)
        deck.insert(2, JOKER_B)
    # If the joker is one up from the bottom card, move it just below the top card
    elif joker_index == (len(deck) - 1) - 1:
        deck.remove(JOKER_B)
        deck.insert(1, JOKER_B)
    # Otherwise, just move the joker two cards down
    else:
        deck.remove(JOKER_B)
        deck.insert(joker_index + 2, JOKER_B)

    return deck

def triple_cut(deck):
    joker_a = deck.index(JOKER_A)
    joker_b = deck.index(JOKER_B)

    if joker_a > joker_b:
        first_joker = joker_b
        second_joker = joker_a
    else:
        first_joker = joker_a
        second_joker = joker_b

    # From beginning to joker A, excluding joker
    above = deck[:first_joker]
    # From joker A to joker B, including jokers
    middle = deck[first_joker:second_joker + 1]
    # From joker B to end, exlcuding joker
    below = deck[second_joker + 1:]

    # Combine the deck, with above and below swapped
    return below + middle + above


def count_cut(deck, count=None):
    bottom_card = deck[len(deck) - 1]
    
    # Convert the jokers into a numerical count
    if bottom_card == "A" or bottom_card == "B":
        bottom_card = "53"

    # When keying the deck with a phrase, we want the option to do a count cut with a specific count rather
    # than using the bottom card. If there is no count given, then proceed with a normal count cut. The top
    # cut still goes at the bottom, above the bottom card!
    if count == None:
        count = int(bottom_card)

    # We will put all the cards at the top of the deck from the beginning to the
    # number specified by the btotom card to the bottom of the deck, above the very
    # last card.
    top_cut = deck[:count + 1]
    # The bottom card should NOT be moved, so that this is reversible.
    rest_cut = deck[count:len(deck) - 1]

    # Reconstruct the deck with the count cut
    deck = rest_cut + top_cut + list(bottom_card)

    return deck
    

if __name__ == "__main__":
    test_deck = ["A", "7", "2", "B", "9", "4", "1"]

    test_deck = move_a_joker(test_deck)
    test_deck = move_b_joker(test_deck)

    print(test_deck)