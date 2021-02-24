from typing import List


class Array:

    def min_size_sub_array(self, target: int, nums: List[int]) -> int:
        """
        Approach: Sliding Window
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param target:
        :param nums:
        :return:
        """
        total = left = right = 0
        res = float("inf")
        while right < len(nums):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res != float("inf") else 0


if __name__ == "__main__":
    array = Array()
    print(array.min_size_sub_array(7, [1, 2, 3, 5, 2, 4]))
    print(array.min_size_sub_array(7, [1, 2, 3, 5, 2, 7]))
    print(array.min_size_sub_array(7, [1, 1, 3, 2, 1, 1]))