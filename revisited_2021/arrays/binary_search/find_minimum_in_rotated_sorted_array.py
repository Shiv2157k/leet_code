from typing import List


class RotateArray:

    def find_minimum(self, nums: List[int]) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        left, right = 0, n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # if pivot right value is less than pivot
            # that's the rotated low value
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            # if pivot is less than pivot - 1
            # return pivot
            if nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            # if the pivot is greater than 1st index value
            # move the left to pivot + 1
            if nums[pivot] > nums[0]:
                left = pivot + 1
            else:
                right = pivot - 1


if __name__ == "__main__":
    sorted_array = RotateArray()
    print(sorted_array.find_minimum([4, 5, 6, 7, 0, 1, 2]))
    print(sorted_array.find_minimum([3, 4, 5, 1, 2]))
    print(sorted_array.find_minimum([0, 1, 2, 4, 5, 6, 7]))
    print(sorted_array.find_minimum([1, 2, 3, 4, 5]))

