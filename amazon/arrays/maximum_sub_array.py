from typing import List


class Array:

    def cross_sum(self, left, right, pivot, nums) -> int:
        """

        :param left:
        :param right:
        :param pivot:
        :param nums:
        :return:
        """
        if left == right:
            return nums[left]

        left_sub_sum = float("-inf")
        current_sum = 0

        for i in range(pivot, left - 1, -1):
            current_sum += nums[i]
            left_sub_sum = max(left_sub_sum, current_sum)

        current_sum = 0
        right_sub_sum = float("-inf")
        for i in range(pivot + 1, right + 1):
            current_sum += nums[i]
            right_sub_sum = max(right_sub_sum, current_sum)

        return left_sub_sum + right_sub_sum

    def helper(self, left: int, right: int, nums: List[int]) -> int:
        """
        :param left:
        :param right:
        :param nums:
        :return:
        """
        if left == right:
            return nums[left]
        pivot = left + (right - left) // 2

        left_sum = self.helper(left, pivot, nums)
        right_sum = self.helper(pivot + 1, right, nums)
        cross_sum = self.cross_sum(left, right, pivot, nums)
        return max(left_sum, right_sum, cross_sum)

    def max_sum_(self, nums: List[int]) -> int:
        """
        Approach: Divide and Conquer
        Time Complexity: O()
        Space Complexity: O()
        :param nums:
        :return:
        """
        return self.helper(0, len(nums) - 1, nums)

    def max_sum(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum


if __name__ == "__main__":
    array = Array()
    print(array.max_sum(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ))
    print(array.max_sum(
        [1]
    ))
    print(array.max_sum(
        [5, 4, -1, 7, 8]
    ))
    print(array.max_sum_(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ))
    print(array.max_sum_(
        [1]
    ))
    print(array.max_sum_(
        [5, 4, -1, 7, 8]
    ))