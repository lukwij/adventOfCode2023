# day03_2.py

from day03_1 import get_numbers_and_symbols, get_positions_to_check


def find_gears(schematics_numbers, schematics_symbols):
    gear_candidates = {}
    for number in schematics_numbers:
        if star_position := is_number_adjacent_to_star(number['row'], number['span'], schematics_symbols):
            if star_position in gear_candidates.keys():
                gear_candidates[star_position].append(number['number'])
            else:
                gear_candidates[star_position] = [number['number']]
    return gear_candidates


def is_number_adjacent_to_star(x_pos, span, symbol_dict: dict):
    star_position: tuple = ()
    for position in get_positions_to_check(x_pos, span):
        if position in symbol_dict.keys():
            if symbol_dict[position] == '*':
                star_position = position
                break
    return star_position


def analyze_gears(gear_candidates: dict) -> int:
    gear_sum = 0
    for key in gear_candidates.keys():
        if len(gear_candidates[key]) == 2:
            gear_sum += gear_candidates[key][0] * gear_candidates[key][1]
    return gear_sum


if __name__ == "__main__":
    numbers, symbols = get_numbers_and_symbols('input')
    print(analyze_gears(find_gears(numbers, symbols)))
