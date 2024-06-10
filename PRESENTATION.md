# Solitaire Cipher

## What is the Solitaire Cipher?
The Solitaire Cipher is a cryptographic algorithm only involving a deck of cards and known information between the sender and receiver. The cipher was designed by Bruce Schneier for Neal Stephenson’s novel Cryptonomicon, where the characters use the Solitaire Cipher to communicate secret messages with each other under the threat of a totalitarian regime. There’s no actual playing Solitaire in this by the way!

## Why a Deck of Cards?
In a totalitarian regime, even access to computers might draw the suspicion of the government. After all, why would a nation loving need a computer of their own? As Schneier describes it however, no one would suspect a simple deck of playing cards. In a government monitoring your every move, cryptography without computers is your safest bet.

## How Does Solitaire Cipher Work?
Essentially, Solitaire Cipher relies on the ordering and shuffling of the deck of cards in order to generate a keystream, which is then used to encrypt a message. The sum of the numerical value of the part of the keystream corresponding to the part of the message mod 26 is the resulting encrypted part.

The only thing needed between the sender and receiver is an agreement upon of protocols for how the deck is ordered, as well as the way in which the deck is initially ordered. Note that this cipher relies on the first order of the deck! If your keyed deck isn’t hard to get to, chances are that cracking the cipher will be simple.

## Some Rules
For the original Solitaire Cipher, we’ll be using an ascending bridge suits order for the order of the cards. The bridge suits order, and the corresponding values is:

* Clubs (+0)
* Diamonds (+13)
* Hearts (+26)
* Spades (+39)
* Jokers (53)

Essentially, these mean that the numerical value of a card is the value written + the value of the suit. Also note that this deck includes the jokers, so you should have 54 cards!

The numerical value of letters are their position in the alphabet.

## Deck Movement
Before we get into the cipher itself, there are some terms regarding deck movement to cover.

**Moving the A Joker**: We will denote one of the jokers as “A”, and this step will move A one card down. In the case that the joker is the bottom card, the joker is the moved below the top card.

**Moving the B Joker**: Another joker denoted as “B”. This time, B is moved two cards down. If the joker is above the bottom card, then it is moved below the top card.

These rules ensure that the deck moves in a cyclical manner, as we will not be discarding any of the cards.

**Triple Cut**: A triple cut is based on the position of the jokers in the deck. All cards that are above the first joker are swapped with the cards that are below the last joker. It doesn’t matter which jokers they are, just their position in the deck. If the jokers are already at the ends of the deck, then there is no change.

**Count Cut**: A count cut uses the numerical value of the bottom card (card # + suit #) based on our established rules. Suppose that the value of the bottom card is n, then we take top n cards, and move them to the bottom, just above the bottom card. If the bottom card is a joker, then the deck is unchanged, since you’d be moving the entire deck except the joker. 

In certain cases, the count cut will rely on a specific number we provide it, rather than solely the bottom card.

## First Steps
Before we do anything with the cipher itself, we need to format the message! 

Since the Solitaire Cipher is limited to a range of 1-26, we will only use uppercase letters for our message, encoding, and decoding. 

In addition, we will be splitting the message into groups of five letters in order to break up any sentence patterns. You can see that the original message is still recognizable, just in a different format.

In the case that a group does not have enough letters to fill out five letters, the rest will be filled in with X’s.

## Keying the Deck
The Solitaire Cipher depends on how we generate the keystream. The keystream process is where the heart of the Solitaire process occurs, and where the initial order of the deck matters. 

It is possible to shuffle a deck however times and send a copy of that deck physically as the key of the cipher. However, this can be cumbersome and prone to human error, so why not just use a phrase instead?

The keying of a deck using a phrase incidentally follows the same Solitaire process as generating the keystream, but the last move is changed up.

The general process of keying a deck for each letter of a phrase is:
* Moving the A joker
* Moving the B joker
* Performing a Triple Cut
* Performing a Count Cut
* Performing a Count Cut again, but the count is the numerical value of the letter

After doing this for all the letter, you should an initial deck ready to be used for the keystream.

## Generating the Keystream
Generating the keystream is just a few additional steps to what we did when keying the deck. Instead of doing the second count cut as we did previously, we will start generating the output character for corresponding parts of the keystream. Your keystream should be the same length as the formatted message!

After performing the first four steps of Solitaire (shown before), the output card is given by the numerical value of the top card of the deck. If the value is n, then we will note the numerical value of the nth card in the deck. The mod 26 of this value will be the numerical value of the letter for the corresponding part of the keystream.

After finding the output, perform Solitaire again! We will keep doing Solitaire for each letter needed of the keystream. This is the main loop of the Solitaire Cipher, and everything that comes afterwards relies on this generated keystream.

## Encrypting
For each character of the message, the encrypted corresponding character is the sum of the numerical values of the message and corresponding keystream letters mod 26. That’s it! The resulting encryption will be grouped in the same way that we grouped the original message letters.

## Decrypting
Decryption of a cipher text is practically the same as decoding, but we subtract the keystream numerical values from message numerical values this time. 

## Shortcomings
And that’s the Solitaire Cipher! An almost secure, practical encryption method that only uses a deck of hard.

However, as many ciphers do, the Solitaire Cipher has issues that come along with the bundle. For one, any mistake made during any part of the cipher can contribute to a larger error when encoding or decoding. This is especially important since this is done by hand, and is prone to human error that computers don’t deal with.

There is also some bias that appears within the cipher’s results. Paul Crowley stated in his analysis of the Solitaire Cipher that one of the largest sources of bias within the cipher is that other cards within the deck happen to be in the same position across the rounds of Solitaire.

This is not intended for large messages!

