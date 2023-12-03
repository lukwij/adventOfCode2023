# day02_1.py

import re


def get_games(filename: str) -> list:
    with open(filename, mode='r') as f:
        for line in f:
            result = re.search(r'Game (\d)+: (.*)$', line)
            pass


if __name__ == "__main__":
    print(get_games('sample'))
