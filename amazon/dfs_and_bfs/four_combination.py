"""
Given an unsorted list of integers, return all combinations
of 4 integers such that a + b + c = z where a, b, c and z are
all integers in given list. Each element of the list may only
be used once in each combination.
Note: No sorting
I/P: [9, 3, 2, 1, 6]
O/P: [1, 2, 3, 6], [1, 2, 6, 9]
"""

from typing import List


class Combination:

    def group_n(self, nums: List[int], n):
        result = []

        def helper(n, arr: List[int], target: int, temp=[]):
            # base cases
            if sum(temp) == target and len(temp) == n - 1:
                result.append(temp + [target])
            elif sum(temp) > target:
                return
            else:
                for idx in range(len(arr)):
                    next_num = arr[idx]
                    new_arr = arr[:idx] + arr[idx + 1:]
                    if not temp or temp[-1] <= next_num:
                        helper(n, new_arr, target, temp + [next_num])

        for i in range(len(nums)):
            target = nums[i]
            arr = nums[:i] + nums[i + 1:]
            helper(n, arr, target)
        return result


if __name__ == "__main__":
    combinations = Combination()
    print(combinations.group_n(
        [9, 3, 2, 1, 6, 5], 3
    ))
