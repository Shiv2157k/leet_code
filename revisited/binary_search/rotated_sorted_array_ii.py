from typing import List


class RotatedSortedArray:

    def exist(self, nums: List[int], target: int) -> bool:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # base condition
            if nums[pivot] == target:
                return True
            # if there exists same values in the rotated sorted array
            # left, right, pivot indices
            # increment left & decrement right by 1
            elif nums[left] == nums[pivot] == nums[right]:
                left += 1
                right -= 1
            # non rotated sorted array
            elif nums[left] <= nums[pivot]:
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            # rotated sorted array
            else:
                if pivot < target <= nums[right]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return False


if __name__ == "__main__":
    array = RotatedSortedArray()
    print(array.exist([1, 3, 1, 1, 1], 3))
    print(array.exist([2, 5, 6, 0, 0, 1, 2], 0))
    print(array.exist([1, 3, 1, 1, 1], 0))
    print(array.exist([2, 5, 6, 0, 0, 1, 2], 3))