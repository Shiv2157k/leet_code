from bisect import bisect_left
from typing import List


class Subsequence:

    def max_sum_subsequence_of_len_k(self, nums: List[int], k: int):
        """
        Approach: Meet in the middle
        Time Complexity: O(n * 2^n/2)
        :param nums:
        :param k:
        :return:
        """
        # generate all the possible sums
        def dfs(idx: int, curr_sum: int, arr: List[int], res: List[int]):

            # base case
            if idx == len(arr):
                res.append(curr_sum)
                return

            # recurse
            # ignore
            dfs(idx + 1, curr_sum, arr, res)
            # pick
            dfs(idx + 1, curr_sum + arr[idx], arr, res)

        sum1, sum2 = [], []
        n = len(nums)

        dfs(0, 0, nums[:n // 2], sum1)
        dfs(0, 0, nums[n // 2:], sum2)

        sum2.sort()
        difference = float("inf")

        # perform binary search
        for s1 in sum1:
            target = k - s1
            pivot = bisect_left(sum2, target)

            # need to perform two operations as our
            # searching number can be in the middle of pivot
            # and pivot - 1
            if pivot < len(sum2):
                difference = min(difference, abs(target - sum2[pivot]))
            if pivot > 0:
                difference = min(difference, abs(target - sum2[pivot - 1]))
        return k - difference


if __name__ == "__main__":
    subsequence = Subsequence()
    print(subsequence.max_sum_subsequence_of_len_k([1, 2, 7, 6, 3, 4, 5, 16], 15))
    print(subsequence.max_sum_subsequence_of_len_k([1, 1, 1, 1, 1, 1, 1], 7))
    print(subsequence.max_sum_subsequence_of_len_k([1, 1, 1, 1, 1, 1, 1], 0))
    print(subsequence.max_sum_subsequence_of_len_k([1, 2, 3, 4, 5], 1))
    print(subsequence.max_sum_subsequence_of_len_k([1, 5, 7, 9, 15], 12))
    print(subsequence.max_sum_subsequence_of_len_k([21, 33, 42, 99, 56], 99))