from typing import List


class MaxSubArray:
    """
    Approach: Divide and Conquer using recursion
    """

    def cross_sum(self, nums: List[int], left: int, right: int, pivot: int) -> int:
        if left == right:
            return nums[left]

        left_sub_sum = float('-inf')
        curr_sum = 0
        for i in range(pivot, left - 1, -1):
            curr_sum += nums[i]
            left_sub_sum = max(curr_sum, left_sub_sum)

        right_sub_sum = float('-inf')
        curr_sum = 0
        for i in range(pivot + 1, right):
            curr_sum += nums[i]
            right_sub_sum = max(curr_sum, right_sub_sum)

        return left_sub_sum + right_sub_sum

    def helper(self, nums: List[int], left: int, right: int) -> int:
        # base case
        if left == right:
            return nums[left]

        pivot = (left + right) // 2
        left_sum = self.helper(nums, left, pivot)
        right_sum = self.helper(nums, pivot + 1, right)
        cross_sum = self.cross_sum(nums, left, right, pivot)

        return max(left_sum, right_sum, cross_sum)

    def max_sub_array(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    ms = MaxSubArray()
    print(ms.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))