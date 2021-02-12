from typing import List


class SortedArray:

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
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            # non - rotated
            elif nums[pivot] >= nums[left]:
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else:
                if nums[right] >= target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1

        return -1


if __name__ == "__main__":
    sorted_array = SortedArray()
    print(sorted_array.search([4, 5, 6, 7, 0, 1, 2], 0))
