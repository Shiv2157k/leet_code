from typing import List


class Array:

    def max_sub_array_sum_with_one_deletion_(self, nums: List[int]) -> int:
        """
        Approach: Left Sum and Right Sum Traverse
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        # for handling negatives
        if max(nums) < 0:
            return max(nums)

        left_sum = [0] * len(nums)
        curr_max = float("-inf")
        for i in range(len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            left_sum[i] = curr_max

        right_sum = [0] * len(nums)
        curr_max = float("-inf")
        best_max = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            curr_max = max(nums[i], curr_max + nums[i])
            best_max = max(best_max, curr_max)  # when considering whole array without deleting
            right_sum[i] = curr_max

        for i in range(1, len(nums) - 2):
            best_max = max(best_max, left_sum[i - 1] + right_sum[i + 1])
        return best_max

    def max_sub_array_sum_with_one_deletion(self, nums: List[int]) -> int:
        """
        Approach: Kadane's Algorithm
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        left_sum = right_sum = cross_sum = float("-inf")
        for num in nums:
            prev_left_sum = left_sum
            left_sum = max(num, left_sum + num)
            right_sum = max(prev_left_sum, right_sum + num)
            cross_sum = max(left_sum, right_sum, cross_sum)
        return cross_sum


if __name__ == "__main__":
    array = Array()
    print(array.max_sub_array_sum_with_one_deletion([1, -2, 0, 3]))
    print(array.max_sub_array_sum_with_one_deletion_([1, -2, 0, 3]))
    print(array.max_sub_array_sum_with_one_deletion([1, -2, -2, 3]))
    print(array.max_sub_array_sum_with_one_deletion_([1, -2, -2, 3]))
    print(array.max_sub_array_sum_with_one_deletion([-1, -1, -1, -1]))
    print(array.max_sub_array_sum_with_one_deletion_([-1, -1, -1, -1]))