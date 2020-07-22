"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""

# Solution w/o deque()
# def sliding_window_max(nums, k):
#     maxes = []
#     i = 0
#     j = i + k - 1

#     while j < len(nums):
#     sliced = nums[i : j + 1]
#         maxes.append(max(sliced))
#         i += 1
#         j += 1

#     return maxes

# Solution w/deque()
import collections


def sliding_window_max(nums, k):
    d = collections.deque()
    maxes = []

    for i, num in enumerate(nums):
        while d and num >= nums[d[-1]]:
            d.pop()
        d += [i]
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            maxes.append(nums[d[0]])

    return maxes


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
