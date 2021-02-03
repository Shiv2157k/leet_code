from typing import List


class Array:

    def max_sub_array_(self, nums: List[int]) -> int:
        """
        Approach: DP (Kadane's algorithm)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum

    def max_sub_array(self, nums: List[int]) -> int:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def get_cross_sum(self, left: int, right: int, pivot: int, nums: List[int]):
        if left == right:
            return nums[left]

        left_sub_sum = float("-inf")
        curr_sum = 0
        for i in range(pivot, left - 1, -1):
            curr_sum += nums[i]
            left_sub_sum = max(curr_sum, left_sub_sum)

        right_sub_sum = float("-inf")
        curr_sum = 0
        for i in range(pivot + 1, right + 1):
            curr_sum += nums[i]
            right_sub_sum = max(curr_sum, right_sub_sum)

        return left_sub_sum + right_sub_sum

    def helper(self, left: int, right: int, nums: List[int]):
        if left == right:
            return nums[left]

        pivot = (left + right) // 2

        left_sum = self.helper(left, pivot, nums)
        right_sum = self.helper(pivot + 1, right, nums)
        cross_sum = self.get_cross_sum(left, right, pivot, nums)

        return max(left_sum, right_sum, cross_sum)

    def get_max_sub_array(self, nums: List[int]) -> int:
        """
        Approach: Divide and Conquer
        Time Complexity: O(N log N)
        Space Complexity: O(log N)
        :param nums:
        :return:
        """
        return self.helper(0, len(nums) - 1, nums)


if __name__ == "__main__":
    array = Array()
    print(array.get_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(array.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
