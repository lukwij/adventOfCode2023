# day01_1.py

import re


def get_numbers(filename: str) -> list:
    with open(filename, mode='r') as f:
        numbers = []
        for line in f:
            result = re.findall(r'\d', line)
            pass
            numbers.append(int(result[0] + result[-1]))
        return numbers


def add_numbers(filename: str) -> int:
    return sum(get_numbers(filename))


if __name__ == "__main__":
    print(add_numbers('input.txt'))
