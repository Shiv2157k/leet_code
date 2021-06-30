from typing import List


class Array:

    def find_pivot_index(self, nums: List[int]) -> int:
        """
        Approach: Prefix Sum
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        total_sum, left_sum = sum(nums), 0

        for pivot_index, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return pivot_index
            left_sum += num
        return -1


if __name__ == "__main__":

    arr = Array()
    print(arr.find_pivot_index([1, 7, 3, 6, 5, 6]))
    print(arr.find_pivot_index([1, 2, 3]))
