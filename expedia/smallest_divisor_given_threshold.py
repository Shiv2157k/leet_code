from typing import List
from math import ceil

class Array:

    def smallest_divisor(self, nums: List[int], threshold: int) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(N log max(N))
        Space Complexity: O(1)
        :param nums:
        :param threshold:
        :return:
        """

        left, right = 1, max(nums) + 1

        def check(div: int):
            total = 0
            for num in nums:
                total += ceil(num / div)
            return total <= threshold

        divisor = 1
        while left < right:
            pivot = left + (right - left) // 2
            if check(pivot):
                right = pivot
                divisor = pivot
            else:
                left = pivot + 1
        return divisor


if __name__ == "__main__":
    array = Array()
    print(array.smallest_divisor([1, 2, 5, 9], 6))
    print(array.smallest_divisor([44, 22, 33, 11, 1], 5))
    print(array.smallest_divisor([21212, 10101, 12121], 1000000))