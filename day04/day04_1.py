# day04_1.py

import re


def check_scratch_cards(filename: str) -> int:
    with open(filename, mode='r') as f:
        pile_score = 0
        for line in f:
            [winning_numbers_string, numbers_to_check_string] = line.split('|')
            winning_numbers = re.findall(r'\d{1,2}(?= )', winning_numbers_string)
            numbers_to_check = re.findall(r'\d+', numbers_to_check_string)

            hit_rate = 0
            for number in numbers_to_check:
                if number in winning_numbers:
                    hit_rate += 1
            if hit_rate > 0:
                pile_score += 2 ** (hit_rate - 1)
        return pile_score


if __name__ == "__main__":
    print(check_scratch_cards('input'))
