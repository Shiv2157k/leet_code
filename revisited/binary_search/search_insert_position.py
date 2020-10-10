from typing import List


class Position:

    def search(self, nums: List[int], target: int) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
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
    position = Position()
    print(position.search([1, 3, 5, 6], 5))
    print(position.search([1, 3, 5, 6], 2))
