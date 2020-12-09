"""
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half
and then the cards in the two halves are perfectly interwoven,
such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
Write a program that receives a single string (cards separated by space) and on the second line receives
a number of faro shuffles that have to be made. Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number
"""
inp = input()
number_of_shuffles = int(input())
# creating a list from string
deck = inp.split()

deck1 = []
deck2 = []

run_cycle = 0

l = int(len(deck) / 2)

while run_cycle < number_of_shuffles:
    # create and/or clear mix desk before the new shuffle
    mix_deck = []
    # set counter for the loop separate in card to 0
    counter = 0
    # separate deck in two halves
    for card in deck:
        if counter < l:
            deck1.append(card)
        elif l <= counter < len(deck):
            deck2.append(card)
        counter += 1
    # mix the two halves/two deck in one new deck
    for i, (a, b) in enumerate(zip(deck1, deck2)):
        mix_deck.append(a)
        mix_deck.append(b)
    # deck = new mix_deck
    deck = []
    for item in mix_deck:
        deck.append(item)
    # clear the deck1 and deck2
    deck1 = []
    deck2 = []

    run_cycle += 1

print(mix_deck)


