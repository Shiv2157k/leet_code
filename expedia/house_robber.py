from typing import List


class HouseRobber:

    def __init__(self):
        self.memo = {}

    def rob_from(self, house: int, nums: List[int]):
        """
        :param house:
        :param nums:
        :return:
        """
        # base case
        if house >= len(nums):
            return 0
        if house in self.memo:
            return self.memo[house]
        money_robbed = max(self.rob_from(house + 1, nums), self.rob_from(house + 2, nums) + nums[house])
        self.memo[house] = money_robbed
        return money_robbed

    def total_robbed__(self, nums: List[int]) -> int:
        """
        Approach: Recursion + Memoization
        :param nums:
        :return:
        """
        return self.rob_from(0, nums)

    def total_robbed_(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def total_robbed(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        rob_curr = nums[0]
        rob_next = nums[1]

        for i in range(2, len(nums)):
            curr = max(rob_curr + nums[i], rob_next)
            rob_curr = rob_next
            rob_next = curr
        return rob_next


if __name__ == "__main__":
    house_robber = HouseRobber()
    # print(house_robber.total_robbed__([2, 7, 9, 3, 1]))
    # print(house_robber.total_robbed__([1, 2, 3, 1]))

    print(house_robber.total_robbed_([2, 7, 9, 3, 1]))
    print(house_robber.total_robbed_([1, 2, 3, 1]))

    print(house_robber.total_robbed([2, 7, 9, 3, 1]))
    print(house_robber.total_robbed([1, 2, 3, 1]))
