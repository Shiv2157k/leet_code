from typing import List


class Array:

    def minimum_size_sub_array(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """

        left = right = total_sum = 0
        size = float("inf")

        while right < len(nums):
            total_sum += nums[right]
            while total_sum >= target:
                size = min(size, right - left + 1)
                total_sum -= nums[left]
                left += 1
            right += 1
        return size if size != float("inf") else 0


if __name__ == "__main__":

    array = Array()
    print(array.minimum_size_sub_array([1, 2, 3, 3, 1], 5))
    print(array.minimum_size_sub_array([1, 2, 2, 3, 4], 4))
    print(array.minimum_size_sub_array([1, 2, 3, 4, 5], 90))