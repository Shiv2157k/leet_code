from typing import List


class RotatedSortedArray:

    def find_num(self, nums: List[int], target: int) -> int:
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

            if nums[pivot] == target:
                return pivot
            elif nums[pivot] >= nums[left]:  # non - rotated
                if nums[left] <= target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            else: # rotated
                if nums[right] >= target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1


if __name__ == "__main__":
    rotated_sorted_arr = RotatedSortedArray()
    print(rotated_sorted_arr.find_num([4, 5, 6, 7, 0, 1, 2], 0))
    print(rotated_sorted_arr.find_num([4, 5, 6, 7, 0, 1, 2], 11))
    print(rotated_sorted_arr.find_num([4, 5, 6, 7, 0, 1, 2], 4))
    print(rotated_sorted_arr.find_num([4, 5, 6, 7, 0, 1, 2], 2))