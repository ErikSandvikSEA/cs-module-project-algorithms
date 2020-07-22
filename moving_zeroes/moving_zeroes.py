"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    length = len(arr)
    if not arr:
        return 0
    counter = 0

    for i in range(length):
        if arr[i] != 0:
            arr[counter] = arr[i]
            counter += 1

    while counter < length:
        arr[counter] = 0
        counter += 1

    return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
