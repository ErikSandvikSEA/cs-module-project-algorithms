"""
Input: an integer
Returns: an integer
"""


# def eating_cookies(n):
#     if n <= 1:
#         return 1
#     if n == 3:
#         return 4
#     if n == 2:
#         return 2

#     else:
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


# attempt w/ cache
def eating_cookies(n, cache=[]):
    if n < 0:
        return 0
    elif n < 2:
        return 1
    elif cache[n] > 0:
        return cache[n]

    else:
        cache[n] = (
            eating_cookies(n - 3, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 1, cache)
        )
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
