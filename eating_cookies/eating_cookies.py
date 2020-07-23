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
import collections


def eating_cookies(n, cache=collections.defaultdict(int)):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if cache[n]:
        return cache[n]

    else:
        cache[n] = (
            eating_cookies(n - 1, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 3, cache)
        )
        return cache[n]


# iterative
# def eating_cookies(n, cache=None):
#     answer = 0
#     c1 = 1
#     c2 = 2
#     c3 = 3
#     for i in range(n - 1):
#         answer = c1 + c2 + c3
#         c3 = c2
#         c2 = c1
#         c1 = answer
#     return answer


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    cache = {}
    print(
        f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies, cache} cookies"
    )
