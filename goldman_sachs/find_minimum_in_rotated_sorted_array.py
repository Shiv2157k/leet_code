from typing import List


class RotatedSortedArray:

    def find_minimum(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]

        left, right = 0, n - 1

        while left <= right:

            pivot = left + (right - left) // 2
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            if nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            if nums[pivot] > nums[0]:
                left = pivot + 1
            else:
                right = pivot - 1


if __name__ == "__main__":
    array = RotatedSortedArray()
    print(array.find_minimum(
        [3, 4, 5, 1, 2]
    ))
    print(array.find_minimum(
        [4, 5, 6, 7, 0, 1, 2]
    ))
    print(array.find_minimum(
        [0, 1, 2, 4, 5, 6, 7]
    ))