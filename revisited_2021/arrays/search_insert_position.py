from typing import List


class Array:

    def search_insert_position(self, nums: List[int], target: int) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(log(N))
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return left


if __name__ == "__main__":
    array = Array()
    print(array.search_insert_position([1, 2, 3, 4, 5], 3))
    print(array.search_insert_position([1, 3, 5, 9], 7))