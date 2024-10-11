from io import DEFAULT_BUFFER_SIZE
from os import initgroups
import re
import sys
from pprint import pprint
import numpy as np

DEFAULT_OFFSET = 0x0000555555554000
file_path = sys.argv[1]
ground_truth = sys.argv[2]


class Predicate:
    address: str
    score: int

    def __init__(self, address, score):
        self.score = round(score, 5)
        self.address = address

    def __str__(self) -> str:
        return f"address: {self.address}, score: {self.score}"


def convert_to_hex(hex_str: str):
    return hex(int(hex_str, 16) - DEFAULT_OFFSET)


def collect_predicates(file_path, ground_truth):
    predicates_list = []
    with open(file_path, "r") as file:
        for line in file.readlines():

            if ground_truth in line:
                line = [x.strip() for x in line.split(" -- ")]
                p = Predicate(convert_to_hex(line[0]), float(line[2]))
                predicates_list.append(p)

    return predicates_list


def avg_list(items):
    if len(items) == 0:
        return 0
    sum = 0
    for item in items:
        sum += item.score
    return sum / len(items)


def divide_into_parts(predicates_list):
    list_len = len(predicates_list)
    scores = [score.score for score in predicates_list]
    if list_len > 0:
        print(" ".join(map(str, scores)))
    if list_len >= 2:
        print([str(x) for x in predicates_list])

        beginning = predicates_list[0].score
        middle = predicates_list[list_len // 2].score
        end = predicates_list[list_len - 1].score

        print(
            str(predicates_list[0])
            + "\n"
            + str(predicates_list[list_len // 2])
            + "\n"
            + str(predicates_list[list_len - 1])
        )
        avg_beginning, avg_middle, avg_end = (
            (beginning),
            (middle),
            (end),
        )
    else:
        print([str(x) for x in predicates_list])


def main():
    divide_into_parts(collect_predicates(file_path, ground_truth))


if __name__ == "__main__":
    main()
