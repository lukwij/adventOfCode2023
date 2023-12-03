# day02_1.py

import re


def get_games(filename: str) -> dict:
    with open(filename, mode='r') as f:
        games = {}
        for line in f:
            result = re.search(r'Game (\d+): (.*)$', line)

            draws = []
            for draw in result.group(2).split(';'):
                pick = {}
                for finding in re.findall(r'(\d+) ([a-z]+)', draw):
                    pass
                    pick[finding[1]] = int(finding[0])
                draws.append(pick)
            games[int(result.group(1))] = draws
        return games


def check_games(condition: dict, input_data: dict) -> int:
    result = 0
    for game_number in input_data.keys():
        game_possible = True
        for pick in input_data[game_number]:
            for color in pick.keys():
                if pick[color] > condition[color]:
                    game_possible = False
                    break
        if game_possible:
            result += game_number
    return result


if __name__ == "__main__":
    game_data = get_games('input')
    print(check_games({'red': 12, 'green': 13, 'blue': 14}, game_data))
