import time
from deck import Deck
from dealer import Hand

# function to define what happens in a round:

def blackjack_round():
    player_hand = Hand(session_deck.deal_card(), session_deck.deal_card())
    dealer_hand = Hand(session_deck.deal_card(), session_deck.deal_card())
    player_hand.calculate_score()
    dealer_hand.calculate_score()

    print('The dealer has: X ' + dealer_hand.hand[1])
    while player_hand.score <= 21:
        player_hand_string = ' '.join(player_hand.hand)
        print('You have: ' + player_hand_string)
        answers = ['h', 's']
        ans = input('What would you like to do?\n'
              '[h]it me! or [s]tay\n')
        if ans not in answers:
            print('invalid response, try again.')
        elif ans == 'h':
            time.sleep(1)
            player_hand.hit_me(session_deck.deal_card())
            player_hand.calculate_score()
        else:
            break
    if player_hand.score > 21:
        player_hand_string = ' '.join(player_hand.hand)
        print('Your hand is: ' + player_hand_string)
        print("Sorry, you busted")
        return

    print("OK, it's the dealer's turn!")
    dealer_hand_string = ' '.join(dealer_hand.hand)
    dealer_hand.calculate_score()
    print(dealer_hand_string)

    while dealer_hand.score <= 21 and dealer_hand.score < player_hand.score:
        new_card = session_deck.deal_card()
        time.sleep(1)
        print(new_card)
        dealer_hand.hit_me(new_card)
        dealer_hand.calculate_score()

    if dealer_hand.score > 21:
        print("The dealer busted. You win!")
    elif dealer_hand.score > player_hand.score:
        print("You lose.")
    elif dealer_hand.score == player_hand.score:
        print("It's a fuckin tie!!")
    return

# starting execution and calling the function:

input('Welcome to blackjack! Press any key to deal.\n')
session_deck = Deck()

exit_code = 0
while exit_code == 0:
    blackjack_round()
    while True:
        ans_list = ['y', 'n']
        x = input('Would you like to play another round? y/n')
        if x not in ans_list:
            print('invalid response')
        elif x == 'n':
            exit_code = 1
            print("Bye!")
        break










