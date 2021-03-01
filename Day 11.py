import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(p_score, c_score):
    if p_score > 21 and c_score > 21:
        return "You went over. You lose"
    if p_score == c_score:
        return 'It is a draw'
    elif c_score == 0 or p_score > 21:
        return 'Computer wins'
    elif p_score == 0 or c_score > 21:
        return 'Player wins'
    elif p_score > c_score:
        return 'Player wins'
    else:
        return 'Computer wins'


def black_jack():
    player_cards = []
    comp_cards = []
    end_game = False
    for _ in range(2):
        player_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not end_game:

        player_score = calculate_score(player_cards)
        comp_score = calculate_score(comp_cards)
        print(player_cards, player_score)
        print(comp_cards, comp_score)

        if player_score > 21 or comp_score == 0 or player_score == 0:
            end_game = True
        else:
            if input('Do you want to draw another card ') == 'y':
                player_cards.append(deal_card())
            else:
                end_game = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f'Your final hand {player_cards} final score {player_score}')
    print(f'Computer final hand {comp_cards}, final score {comp_score}')

    print(compare(player_score, comp_score))

    if input("Do you want to play again? answer 'y' or 'n'") == 'y':
        black_jack()


black_jack()
