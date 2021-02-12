from typing import List


class SortedArray:

    def index(self, nums: List[int], target: int, is_left: bool) -> int:
        left, right = 0, len(nums)
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] > target or (is_left and nums[pivot] == target):
                right = pivot
            else:
                left = pivot + 1
        return left

    def first_and_last_element(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        left_index = self.index(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.index(nums, target, False) - 1]


if __name__ == "__main__":
    array = SortedArray()
    print(array.first_and_last_element([1, 1, 2, 2, 4, 9, 9, 11], 9))