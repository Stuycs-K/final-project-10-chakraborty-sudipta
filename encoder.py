import deck_moves
import sys

LETTER_A_DEC = 65
LETTER_A_OFFSET = LETTER_A_DEC - 1
FILLER_LETTER = "X"
GROUP_LETTER_COUNT = 5

# NOTE: This encoder only uses capital letters!
# The input should be capitalized, and the program will capitalize it anyways
# if it isn't. The output will also be capitalized. This includes the key as well.abs

def split_message(message):
    message = message.upper()
    groups = [""]
    group_index = 0
    group_string_index = 0

    # Split the message into groups of 5, to break up any sentence patterns and ensure security
    for index in range(len(message)):
        if message[index].isalpha():
            groups[group_index] += message[index]
            group_string_index = 0
            
            # If the current group is full, move on to the next one
            if len(groups[group_index]) == GROUP_LETTER_COUNT:
                group_index += 1
                group_string_index = 0

                if index != len(message) - 1:
                    groups.append("")

    # If the last group does not have 5 letters, fill in the remaining spots with "X"
    groups[-1] = groups[-1] + (FILLER_LETTER * (GROUP_LETTER_COUNT - len(groups[-1])))
    return groups

    
def letter_as_num(letter):
    return ord(letter) - LETTER_A_DEC + 1

def key_as_deck(key):
    key = key.upper()

    deck = deck_moves.get_fixed_deck()

    # We perform the same Solitaire steps as we would when encoding. HOWEVER, we do a second count cut based on
    # the corresponding letter of the key.
    for letter in key:
        deck = deck_moves.move_a_joker(deck)
        deck = deck_moves.move_b_joker(deck)
        deck = deck_moves.triple_cut(deck)
        deck = deck_moves.count_cut(deck)
        deck = deck_moves.count_cut(deck, count=letter_as_num(letter))

    return deck


# Generation of the keystream using the deck of card
def keystream_gen(message, key, length):
    # The deck of cards, as an alphanumerical representation.
    # NOTE: This deck includes the Jokers, which is important for the keystream generation.
    # The order of this deck matters! It determines the rest of what happens. Shuffling the
    # deck also works here, but the shuffled order must be sent to the recipient too.
    deck = key_as_deck(key)
    keystream = ""
    
    # These steps will be repeated for each letter of the message.
    for _ in range(length):
        is_joker = True
        
        # The joker should not be used in the keystream, so we will loop this until the output is not a joker.
        while is_joker:
            # Perform the initial steps of solitaire, which involve moving the jokers.
            deck = deck_moves.move_a_joker(deck)
            deck = deck_moves.move_b_joker(deck)
            deck = deck_moves.triple_cut(deck)
            deck = deck_moves.count_cut(deck)
            if deck[-1] != "A" and deck[-1] != "B":
                is_joker = False
            # Otherwise, keep performing Solitaire

        top_card = deck[0]

        if top_card == "A" or top_card == "B":
            output_int = 53
        else:
            output_int = int(top_card)

        # We convert the 1-53 scale to a 1-26 scale so that the output can be converted to a character.
        output_int = output_int % 26
        keystream += chr(output_int + LETTER_A_OFFSET)

    return keystream


def encode(message, key, decode=False):
    message_groups = split_message(message)
    # The length of the keystream should be the same as the groups of the message
    keystream = keystream_gen(message, key, len(message_groups) * GROUP_LETTER_COUNT)
    keystream_groups = split_message(keystream)
    # keystream_groups = ["KDWUP", "ONOWT"]
    encoded_groups = [""] * len(message_groups) 

    if decode:
        multiplier = -1
    else:
        multiplier = 1

    for group_index in range(len(message_groups)):
        for letter_index in range(GROUP_LETTER_COUNT):
            message_letter_num = letter_as_num(message_groups[group_index][letter_index])
            keystream_letter_num = letter_as_num(keystream_groups[group_index][letter_index])

            if decode:
                if message_letter_num < keystream_letter_num:
                    message_letter_num += 26

            part = (message_letter_num + (multiplier * keystream_letter_num)) % 26
            encoded_groups[group_index] += chr(part + LETTER_A_OFFSET)

    return " ".join(encoded_groups)

if __name__ == "__main__":
    message = sys.argv[1]
    key = sys.argv[2]

    print(encode(message, key))

