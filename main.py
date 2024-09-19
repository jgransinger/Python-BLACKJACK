import random
import art

def deal_cards():
    """Assigns two random values from 'cards' to player and one to dealer"""
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

def calc_cards():
    global player_total
    global dealer_total
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    # print(f"Player: {player_total} ||  Dealer: {dealer_total}")
    if player_total == 21 and dealer_total != 21:
        player_has_blackjack()
    if dealer_total == 21 and player_total != 21:
        dealer_has_blackjack()
    if dealer_total == 21 and player_total == 21:
        draw()
    if player_total > 21:
        for each_card in player_cards:
            if each_card == 11:
                player_cards.remove(each_card)
                player_cards.append(1)
                player_total = sum(player_cards)
                print(f"Ace reduced from 11 to 1. Total is now: {player_total}")
                print(f"Player: {player_total} ||  Dealer: {dealer_total}")
                print(player_cards)
    if player_total > 21:
        player_bust()
    if player_total < 21:
        draw_card()

def add_card():
    player_cards.append(random.choice(cards))
    print(f"Your cards are: {player_cards}")

def show_cards():
    print(f"Your cards: {player_cards}")
    print(f"Dealer Card: {dealer_cards[0]}")

def show_total():
    print(f"Player: {player_total} ||  Dealer: {dealer_total}")

def player_has_blackjack():
    show_total()
    print("You hit blackjack! You WIN!")
    global game_over
    game_over = True
    play_again()

def dealer_has_blackjack():
    show_total()
    print("The dealer has a total of 21. You LOSE.")
    global game_over
    game_over = True
    play_again()

def draw():
    show_total()
    print("Dealer and Player both have 21. DRAW.")
    global game_over
    game_over = True
    play_again()

def player_bust():
    show_total()
    print(f"BUST. You went over 21! you LOSE.")
    global game_over
    game_over = True
    play_again()

def dealer_bust():
    show_total()
    print(f"The dealer has BUSTED. You WIN.")
    global game_over
    game_over = True
    play_again()

def draw_card():
    while not game_over:
        ask_draw_card = input("Do you want to draw a new card?: (y/n:) \n").lower()
        if ask_draw_card == "y":
            add_card()
            calc_cards()
        if ask_draw_card == "n":
            print(f"Your total is: {player_total}.")
            dealer_card_flip()
            dealer_calc()

def dealer_card_flip():
    dealer_cards.append(random.choice(cards))

def dealer_calc():
    global dealer_total
    print(f"Dealers cards: {dealer_cards}")
    dealer_total = sum(dealer_cards)
    if dealer_total < 17:
        print("Dealer draws a card.....")
        dealer_cards.append(random.choice(cards))
        dealer_total = sum(dealer_cards)
        dealer_calc()
    elif dealer_total >= 17 and dealer_total <= 21 and dealer_total > player_total:
        print(f"Dealer final total: {dealer_total}.")
        final_score()
    elif dealer_total >= 17 and dealer_total <= 21 and dealer_total == player_total:
        print(f"Dealer final total: {dealer_total}.")
        final_score()
    elif dealer_total >= 17 and dealer_total <= 21 and dealer_total < player_total:
        print("Dealer draws a card.....")
        dealer_cards.append(random.choice(cards))
        dealer_total = sum(dealer_cards)
        dealer_calc()
    elif dealer_total == 21:
        dealer_has_blackjack()
    elif dealer_total > 21:
        if dealer_total > 21:
            for each_card in dealer_cards:
                if each_card == 11:
                    dealer_cards.remove(each_card)
                    dealer_cards.append(1)
                    dealer_total = sum(dealer_cards)
                    print(f"Ace reduced from 11 to 1. Total is now: {dealer_total}")
                    print(f"Dealer cards: {dealer_cards}")
                    dealer_calc()
        if dealer_total > 21:
            dealer_bust()

def final_score():
    global game_over
    if player_total > dealer_total:
        show_total()
        print("You win!")
        play_again()
    elif player_total < dealer_total:
        show_total()
        print("You lose!")
        play_again()
    else:
        show_total()
        print("Draw!")
        play_again()
    game_over = True

def play_again():
    play_again = input("Would you like to play again?: (y/n): ")
    if play_again == "y":
        print("\n" * 2)
        print(art.logo)
        print("\n" * 2)
        global dealer_cards, player_cards, game_over
        dealer_cards = []
        player_cards = []
        game_over = False

        deal_cards()
        show_cards()
        calc_cards()
    else:
        print("Game ended.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []
player_total = sum(player_cards)
dealer_total = sum(dealer_cards)
game_over = False

#### GAME BEGINS #####
#### GAME BEGINS #####
#### GAME BEGINS #####

print(art.logo)
print("\n")
start_game = input("Howdy Partner, fancy a game of blackjack?: (y/n): \n").lower()
if start_game == "y":
    deal_cards()
    show_cards()
    calc_cards()
else:
    print("Kind of rude but okay. bye, i guess.")

