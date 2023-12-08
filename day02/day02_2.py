# day02_2.py

from day02_1 import get_games
from math import prod


def check_games(input_data: dict) -> int:
    result = 0
    for game_number in input_data.keys():
        min_game_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for pick in input_data[game_number]:
            for color in pick.keys():
                if pick[color] > min_game_cubes[color]:
                    min_game_cubes[color] = pick[color]
        game_score = prod(min_game_cubes.values())
        result += game_score
    return result


if __name__ == "__main__":
    game_data = get_games('input')
    print(check_games(game_data))
