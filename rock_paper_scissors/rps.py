#!/usr/bin/python

import sys
import collections


def rock_paper_scissors(n, cache=collections.defaultdict(str)):
    # establish possible plays and result arr
    possible_plays = ["rock", "paper", "scissors"]
    results = []

    # helper function
    def choice(rounds_remaining, round_result):
        if rounds_remaining == 0:
            results.append(round_result)
            return

        for i in range(len(possible_plays)):
            choice(rounds_remaining - 1, round_result + [possible_plays[i]])

    choice(n, [])
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(len(rock_paper_scissors(num_plays)))
    else:
        print("Usage: rps.py [num_plays]")

