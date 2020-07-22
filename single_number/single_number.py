"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


def single_number(arr):
    import collections

    counter = collections.defaultdict(int)

    for elem in arr:
        counter[elem] += 1

    for key, val in counter.items():
        if val < 2:
            return key


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
