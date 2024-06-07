JOKER_A = "A"
JOKER_B = "B"

# Bridge suits order is spades, hearts, diamonds, clubs
def get_deck():
    return [str(card) for card in range(1, 52 + 1)] + ["A", "B"]

def letter_as_num(letter):
    LETTER_A_DEC = 65
    return ord(letter) - LETTER_A_DEC


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

# TODO: first_joker and second_joker should NOT be dependent on which joker it is!
def triple_cut(deck):
    first_joker = deck.index(JOKER_A)
    second_joker = deck.index(JOKER_B)

    # From beginning to joker A, excluding joker
    above = deck[:first_joker]
    # From joker A to joker B, including jokers
    middle = deck[first_joker:second_joker + 1]
    # From joker B to end, exlcuding joker
    below = deck[second_joker + 1:]

    # Combine the deck, with above and below swapped
    return below + middle + above


def count_cut(deck):
    ...

test_deck = ["A", "7", "2", "B", "9", "4", "1"]

test_deck = move_a_joker(test_deck)
test_deck = move_b_joker(test_deck)

print(test_deck)