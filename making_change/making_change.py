#!/usr/bin/python

import sys
import collections

# walkthrough code from educative.io


def making_change(amount, denominations):
    num_of_coins = len(denominations)

    arr = [[0] * (amount + 1) for i in range(num_of_coins + 1)]

    for j in range(num_of_coins + 1):
        arr[j][0] = 1

    for k in range(1, num_of_coins + 1):
        for m in range(1, amount + 1):
            if denominations[k - 1] > m:
                arr[k][m] = arr[k - 1][m]
            else:
                arr[k][m] = arr[k - 1][m] + arr[k][m - denominations[k - 1]]
    return arr[num_of_coins][amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")

