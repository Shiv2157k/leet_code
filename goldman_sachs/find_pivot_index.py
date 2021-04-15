from typing import List


class Array:

    def find_pivot_index(self, nums: List[int]) -> int:
        """
        Approach: Prefix Sum
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        # total_sum = sum(nums)
        total_sum = left_sum = 0
        for num in nums:
            total_sum += num

        for pivot, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return pivot
            left_sum += num
        return -1


if __name__ == "__main__":
    array = Array()
    print(array.find_pivot_index([1, 7, 3, 6, 5, 6]))
    print(array.find_pivot_index([2, -1, 1]))
    print(array.find_pivot_index([2, 1, 2]))
    print(array.find_pivot_index([1, 1]))