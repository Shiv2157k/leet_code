from typing import List


class SortedArray:

    def find_index(self, nums: List[int], target: int, is_left: bool) -> List[int]:
        """
        To find indexed of first and last position of target in
        repeated sorted array.
        :param nums:
        :param target:
        :param is_left:
        :return:
        """
        left, right = 0, len(nums)
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] > target or (is_left and nums[pivot] == target):
                right = pivot
            else:
                left = pivot + 1
        return left

    def get_first_and_last_position(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Binary Search Modified
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        left_index = self.find_index(nums, target, True)

        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.find_index(nums, target, False) - 1]


if __name__ == "__main__":

    sorted_array = SortedArray()
    print(sorted_array.get_first_and_last_position([5, 7, 7, 8, 8, 10], 8))
    print(sorted_array.get_first_and_last_position([5, 7, 7, 8, 8, 10], 9))
    print(sorted_array.get_first_and_last_position([5, 7, 7, 8, 8, 10], 5))
    print(sorted_array.get_first_and_last_position([5, 7, 7, 8, 8, 10], 7))