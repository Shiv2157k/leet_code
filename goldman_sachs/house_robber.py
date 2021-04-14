from typing import List


class Houses:

    def __init__(self):
        self.memo = {}

    def total_money_robbed_recursion(self, nums: List[int]) -> int:
        """
        Approach: Recursion with Memoization
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        return self.rob_from(0, nums)

    def rob_from(self, house: int, nums: List[int]) -> int:
        """
        Recursion Function
        :param house:
        :param nums:
        :return:
        """
        # base case
        # if there is no more houses
        if house >= len(nums):
            return 0

        # memoization
        if house in self.memo:
            return self.memo[house]

        # recursion
        money_robbed = max(self.rob_from(house + 1, nums), self.rob_from(house + 2, nums) + nums[house])

        # store in the cache
        self.memo[house] = money_robbed

        return money_robbed

    def total_money_robbed_dp(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        # base case
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for house in range(2, len(nums)):
            dp[house] = max(dp[house - 2] + nums[house], dp[house - 1])
        return dp[-1]

    def total_money_robbed_dp_optimized(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        # edge cases
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        current_rob = nums[0]
        next_rob = max(nums[0], nums[1])

        for house in range(2, len(nums)):

            current = max(current_rob + nums[house], next_rob)

            current_rob = next_rob
            next_rob = current
        return next_rob


if __name__ == "__main__":
    house_robber = Houses()
    print(house_robber.total_money_robbed_dp([1, 2, 3, 1]))
    print(house_robber.total_money_robbed_dp_optimized([1, 2, 3, 1]))
    print(house_robber.total_money_robbed_recursion([1, 2, 3, 1]))
