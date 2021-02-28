from typing import List


class Array:

    def can_partition(self, nums: List[int]) -> bool:
        """
        Approach: DP (1D Array)
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        :param nums:
        :return:
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        sub_set_sum = total_sum // 2
        dp = [False] * (sub_set_sum + 1)
        dp[0] = True
        for num in nums:
            for j in range(sub_set_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[sub_set_sum]

    def can_partition_(self, nums: List[int]) -> bool:
        """
        Approach: DP (2D Array)
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        :param nums:
        :return:
        """
        total_sum = sum(nums)
        # if it is odd never can be partitioned into equal subset sum
        if total_sum % 2 != 0:
            return False
        sub_set_sum = total_sum // 2
        n = len(nums)
        # build the dp array with subset and length of nums
        dp = [[False] * (sub_set_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(sub_set_sum + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[n][sub_set_sum]


if __name__ == "__main__":
    array = Array()
    print(array.can_partition_([2, 3, 7, 8, 10]))
    print(array.can_partition_([1, 1, 1, 1, 1]))
    print(array.can_partition([2, 3, 7, 8, 10]))
    print(array.can_partition([1, 1, 1, 1, 1]))