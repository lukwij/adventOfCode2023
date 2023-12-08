# day04_1.py

import re


def get_scratch_cards(filename: str) -> list:
    with open(filename, mode='r') as f:
        scratch_cards = []
        for line in f:
            [winning_numbers_string, numbers_to_check_string] = line.split('|')
            winning_numbers = re.findall(r'\d{1,2}(?= )', winning_numbers_string)
            numbers_to_check = re.findall(r'\d+', numbers_to_check_string)
            scratch_cards.append({'quantity': 1, 'winning': winning_numbers, 'numbers': numbers_to_check})
        return scratch_cards


def check_cards(cards: list) -> list:
    cards_qty = len(cards)
    for card_no, card in enumerate(cards):
        hit_rate = 0
        for number in card['numbers']:
            if number in card['winning']:
                hit_rate += 1

        for _ in range(card['quantity']):
            for i in range(1, hit_rate + 1):
                if (card_no + i + 1) > cards_qty:
                    break
                cards[card_no + i]['quantity'] += 1
        pass
    return cards


def count_card(cards: list) -> int:
    return sum([card['quantity'] for card in cards])


if __name__ == "__main__":
    cards = get_scratch_cards('input')
    print(count_card(check_cards(cards)))
