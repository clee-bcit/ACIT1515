# blackjack.py assignment
# ACIT1515 - Set B
# Chris Chanwoo Lee
# A01016225

import cards
    
def start_game():
    deck = cards.make_deck()
    cards.shuffle_deck(deck)
    player_hand = []
    dealer_hand = []
    player_hand.append(cards.deal_card(deck))
    dealer_hand.append(cards.deal_card(deck))
    player_hand.append(cards.deal_card(deck))
    dealer_hand.append(cards.deal_card(deck))
    
    print_hand("Player's Hand: ", player_hand)
    print_hand("Dealer's Hand: ", dealer_hand)

    user_input = input('Hit (H) or Stand? (S): ')
    while user_input[0].upper() == 'H':
        player_hand.append(cards.deal_card(deck))
        print_hand("Player's Hand: ", player_hand)
        print_hand("Dealer's Hand: ", dealer_hand)
        if calc_score(player_hand) > 21:
            break
        user_input = input('Hit (H) or Stand (S): ')
        
    while calc_score(dealer_hand) <= 16 and calc_score(player_hand) < 22 and calc_score(dealer_hand) < calc_score(player_hand):
        dealer_hand.append(cards.deal_card(deck))
        
    print_hand("Dealer's Hand: ", dealer_hand)
    
    result = ""
    player_score = calc_score(player_hand)
    dealer_score = calc_score(dealer_hand)
    if player_score == dealer_score:
        print("It's a tie")
        result = 'tie'
    elif (player_score <= 21 and player_score > dealer_score) or (dealer_score > 21):
        print("Player win")
        result = 'player'
        
    else:
        print("Player lose")
        result = 'dealer'
        
    return result


def print_hand(desc, hand):
    print(f'{desc} : {hand}')
    

def calc_score(hand):
    score = 0
    for card in hand:
        score += cards.CARD_SCORES[card.value]
        
    for card in hand:
        if card.value == "Ace" and score >21:
            score -= 10
    
    return score

def main():
    wins = 0
    losses = 0
    ties = 0
    keep_playing = True
    while keep_playing == True:
        # operation
        result = start_game()
        if result == 'player':
            wins += 1
        elif result == 'dealer':
            losses += 1
        else:
            ties += 1
        # get out of the loop
        user_choice = input("Would you like to play again(Y/N)? ")
        if user_choice[0].upper() != 'Y':
            keep_playing = False

    print(f'Wins: {wins} Losses: {losses}')


if __name__ == '__main__':
    main()

