from typing import List


class Array:

    def cross_sum(self, left: int, right: int, nums: List[int], pivot: int) -> int:
        """
        Calculates the cross sum.
        :param left:
        :param right:
        :param nums:
        :return:
        """
        if left == right:
            return nums[left]

        left_sub_sum = float("-inf")
        curr_sum = 0
        for i in range(pivot, left - 1, -1):
            curr_sum += nums[i]
            left_sub_sum = max(left_sub_sum, curr_sum)

        right_sub_sum = float("-inf")
        curr_sum = 0
        for i in range(pivot + 1, right + 1):
            curr_sum += nums[i]
            right_sub_sum = max(right_sub_sum, curr_sum)
        return left_sub_sum + right_sub_sum

    def helper(self, left: int, right: int, nums: List[int]) -> int:
        """
        Helper function that sub divides into left sum, right sum and
        cross sum
        :param left:
        :param right:
        :param nums:
        :return:
        """
        if left == right:
            return nums[left]

        pivot = (left + right) // 2

        left_sum = self.helper(left, pivot, nums)
        right_sum = self.helper(pivot + 1, right, nums)
        cross_sum = self.cross_sum(left, right, nums, pivot)

        return max(left_sum, cross_sum, right_sum)

    def get_max_sub_array(self, nums: List[int]) -> int:
        """
        Approach: Divide and Conquer
        Time Complexity: O(N log N)
        Space Complexity: O(log N)
        :param nums:
        :return:
        """
        return self.helper(0, len(nums) - 1, nums)

    def get_max_sub_array_(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        curr_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def get_max_sub_array__(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm or DP
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        max_sum = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx - 1] > 0:
                nums[idx] += nums[idx - 1]
            max_sum = max(max_sum, nums[idx])
        return max_sum


if __name__ == "__main__":
    array = Array()
    print(array.get_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(array.get_max_sub_array_([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(array.get_max_sub_array__([-2, 1, -3, 4, -1, 2, 1, -5, 4]))