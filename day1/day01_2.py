# day01_2.py

import re
from word2number import w2n


def get_numbers(filename: str) -> list:
    with open(filename, mode='r') as f:
        numbers = []
        pattern = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)')

        for line in f:
            first_digit = w2n.word_to_num(pattern.search(line).group(0))
            second_digit = None
            for i in range(len(line)):
                if pattern.search(line[i:]):
                    second_digit = w2n.word_to_num(pattern.search(line[i:]).group(0))
                    
            numbers.append(int(first_digit * 10 + second_digit))
        return numbers


def add_numbers(filename: str) -> int:
    return sum(get_numbers(filename))


if __name__ == '__main__':
    print(add_numbers('input.txt'))
