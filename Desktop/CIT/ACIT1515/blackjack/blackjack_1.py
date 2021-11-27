# First: all programs require a header block with the info from next 2 lines...
# Author: Playerr name, student number, set, and the course
# Date: the day Player wrote the program


# imports come first, after the header block (leave two lines after the imports)  

import cards
import getpass

    
# display cards
# sum of the dealer cards
# sum of the player cards
# compare sum of the cards 
# if P card sum is > 21 = bust/lose
# if P card sum < 21 = hit or stay 
# if P stay compare sum of D and P 
# if P sum < 21 > D sum = P wins
# if P sum < D sum = P loses 
def print_hand(desc, hand):
    print(f'{desc} : {hand}')


def play_game():
    "Creates deck, shuffles, and deals. Get 2 cards each for the player and dealer."
    deck = cards.make_deck()
    cards.shuffle_deck(deck)
    player_hand = []
    dealer_hand = []
    player_hand.append(cards.deal_card(deck))
    player_hand.append(cards.deal_card(deck))
    dealer_hand.append(cards.deal_card(deck))
    dealer_hand.append(cards.deal_card(deck))

    print_hand('Player Hand', player_hand)
    print_hand('Dealers Hand', dealer_hand)

    user_input = input('Hit (H) or Stand? (S): ') 
    while user_input[0].upper() == 'H':
        player_hand.append(cards.deal_card(deck))
        print_hand('Player Hand', player_hand)
        print_hand('Dealers Hand', dealer_hand)
        if cal_score(player_hand) > 21: 
            break
        user_input = input('Hit (H) or Stand? (S): ') 


    while cal_score(dealer_hand) <= 16 and cal_score(player_hand) < 22 and cal_score(dealer_hand) < cal_score(player_hand): 
        dealer_hand.append(cards.deal_card(deck))
    
    print_hand('Dealer Hand', dealer_hand)

    result = ""
    player_score = cal_score(player_hand)
    dealer_score = cal_score(dealer_hand)
    if player_score == dealer_score:
        print("Tie")
        result = 'tie'
    elif (player_score <= 21 and player_score > dealer_score) or (dealer_score > 21):
        print("Player win")
        result = 'player'
    else:
        print("Player lose")
        result = 'dealer'

    return result



def cal_score(hand):
    score = 0
    for card in hand:
        score += cards.CARD_SCORES[card.value]
    
    for card in hand:
        if card.value == "Ace" and score > 21:
                score -= 10 

    return score 


    
# main function
# typically contains the 'main' body of code, which could be some tests that
# will be run, or could be the 'main algorithm' for the program
def main():
  
    
    wins = 0
    losses = 0
    ties = 0
    keep_playing = True
    while keep_playing:
        result = play_game()
        if result == 'player':
            wins += 1
        elif result == 'dealer': 
            losses += 0 
        else:
            ties +=0
        
        user_choice = input("Would you like to play again? (Y/N)")
        if user_choice[0].upper() != 'Y':
            keep_playing = False 
    print(f'Wins: {wins} Losses: {losses}')





# Only execute main if the program is loaded by the interpreter directly
# i.e. not imported 
if __name__ == '__main__':
    main()   # this line is what starts execution, followed by a single blank line





