from typing import List


class Array:

    def find_duplicate(self, nums: List[int]) -> int:
        """
        # 1 -> using sort T: O(n log n) S: O(1)
        # 2 -> using set T: O(N) S: O(N)
        Approach: Floyd's (Hare & Tortoise) Algorithm
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        tortoise = hare = nums[0]
        # phase 1: find the intersection
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        # phase 2: find entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare


if __name__ == "__main__":
    array = Array()
    print(array.find_duplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
    print(array.find_duplicate([2, 5, 9, 6, 7, 3, 8, 7, 7, 1]))
    print(array.find_duplicate([2, 5, 9, 6, 2, 3, 8, 2, 7, 1]))