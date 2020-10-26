from typing import List


class RotatedSortedArray:

    def search(self, nums: List[int], target: int) -> int:
        """
        Approach: One Pass Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """

        left, right = 0, len(nums) - 1

        # binary search
        while left <= right:

            # pivot
            pivot = left + (right - left) // 2

            # if you have found the target return the index
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= nums[left]:  # condition for non sorted array
                if nums[left] <= target < nums[pivot]:  # move the right to pivot
                    right = pivot - 1
                else:  # move the left to pivot
                    left = pivot + 1
            else:
                if nums[right] >= target > nums[pivot]:  # move the left to pivot
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1  # no element found


if __name__ == "__main__":

    rotated_array = RotatedSortedArray()
    print(rotated_array.search([4, 5, 6, 7, 8, 1, 2, 3], 1))
    print(rotated_array.search([4, 5, 6, 7, 8, 1, 2, 3], 3))
    print(rotated_array.search([4, 5, 6, 7, 8, 1, 2, 3], 5))
    print(rotated_array.search([4, 5, 6, 7, 8, 1, 2, 3], 9))