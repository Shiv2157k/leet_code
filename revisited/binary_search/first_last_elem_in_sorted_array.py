from typing import List


class SortedArray:

    def find_index(self, nums: List[int], target: int, is_left: bool) -> int:
        """
        Binary Search to get the start and end index of target.
        :param nums:
        :param target:
        :param is_left:
        :return:
        """
        left, right = 0, len(nums)
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] > target or (is_left and nums[pivot] == target):
                right = pivot
            else:
                left = pivot + 1
        return left

    def find_first_and_last_element(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        left_index = self.find_index(nums, target, True)
        # base case
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.find_index(nums, target, False) - 1]


if __name__ == "__main__":
    sorted_array = SortedArray()
    print(sorted_array.find_first_and_last_element([1, 2, 4, 7, 7, 7, 9, 11], 7))
    print(sorted_array.find_first_and_last_element([7, 7, 7], 7))
    print(sorted_array.find_first_and_last_element([9, 11], 9))
    print(sorted_array.find_first_and_last_element([9, 9, 11], 9))
    print(sorted_array.find_first_and_last_element([9, 9, 11], 7))