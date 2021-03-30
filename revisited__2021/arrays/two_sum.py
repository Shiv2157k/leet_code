from typing import List


class Array:

    def two_sum_index(self, nums: List[int], target: int):
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        if not nums:
            return []
        hash_map = {}

        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i


if __name__ == "__main__":
    array = Array()
    print(array.two_sum_index(
        [2, 7, 11, 5], 9
    ))
    print(array.two_sum_index(
        [3, 2, 4], 6
    ))