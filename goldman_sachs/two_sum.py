from typing import List


class Array:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :param target:
        :return:
        """
        look_up = {}
        for index, num in enumerate(nums):
            if target - num in look_up:
                return [look_up[target - num], index]
            else:
                look_up[num] = index


if __name__ == "__main__":
    array = Array()
    print(array.two_sum([2, 7, 11, 15], 9))
    print(array.two_sum([3, 2, 4], 6))
    print(array.two_sum([3, 3], 6))