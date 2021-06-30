from functools import lru_cache
from typing import List, Tuple


class Array:

    def can_partition_equal_subset_sum__(self, nums: List[int]) -> bool:
        """
        Approach: DP - 1D Array Bottom Up
        Time Complexity: O(M * N)
        Space Complexity: O(M)
        :param nums:
        :return:
        """

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        dp = [False] * (subset_sum + 1)
        dp[0] = True

        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
        return dp[subset_sum]

    def can_partition_equal_subset_sum_(self, nums: List[int]) -> bool:
        """
        Approach: DP - Bottom Up
        Time Complexity: O(M * N)
        Space Complexity: O(M * N)
        :param nums:
        :return:
        """

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]

    def can_partition_equal_subset_sum(self, nums: List[int]) -> bool:
        """
        Approach: DP - Top Down Approach
        Time Complexity:
        Space Complexity:
        :param nums:
        :return:
        """

        @lru_cache(maxsize=None)
        def dfs(nums: Tuple[int], n: int, subset_sum: int):
            # base case
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False

            result = (dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum))
            return result

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)


if __name__ == "__main__":
    array = Array()
    print(array.can_partition_equal_subset_sum([1, 5, 11, 5]))
    print(array.can_partition_equal_subset_sum([1, 2, 3, 4, 5]))

    print(array.can_partition_equal_subset_sum__([1, 5, 11, 5]))
    print(array.can_partition_equal_subset_sum__([1, 2, 3, 4, 5]))

    print(array.can_partition_equal_subset_sum_([1, 5, 11, 5]))
    print(array.can_partition_equal_subset_sum_([1, 2, 3, 4, 5]))
