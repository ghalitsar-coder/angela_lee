from utils.functions import generate_number_max_11, getReminderNumber


def blackjack():
    result = ""
    print("Lets play black jack !")
    our_cards = [generate_number_max_11(), generate_number_max_11()]
    dealer_cards = [generate_number_max_11(), generate_number_max_11()]
    print(f"Your Cards {our_cards}")
    print(f"Computer First Card {dealer_cards[0]}")
    get_another_card = input("Do you want to get another card ? (y/n): ").lower()
    if get_another_card == "y":
        our_cards.append(generate_number_max_11())

    print(f"Your Cards {our_cards} = {sum(our_cards)}")
    print(f"Computer Cards {dealer_cards} = {sum(dealer_cards)}")
    if sum(our_cards) <= 21:
        player_num = getReminderNumber(our_cards)
        comp_num = getReminderNumber(dealer_cards)
        if player_num == comp_num:
            result = "DRAW!!"
        result = "You Win!" if player_num < comp_num else "You Lose!"
    else:
        result = "You went over 21, you lose"
    return result


print(blackjack())
