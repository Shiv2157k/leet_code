from typing import List


class MaxSub:

    def max_sub(self, nums: List[int]) -> int:
        """
        Approach: Greedy Algorithm
        :param nums:
        :return:
        """
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum

    def max_sub_(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm
        :param nums:
        :return:
        """
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(max_sum, nums[i])
        return max_sum


if __name__ == "__main__":
    ms = MaxSub()
    print(ms.max_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(ms.max_sub_([-2, 1, -3, 4, -1, 2, 1, -5, 4]))