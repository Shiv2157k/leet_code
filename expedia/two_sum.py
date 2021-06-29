from typing import List


class TwoSum:

    def find_index(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Hash Table
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """

        hash_map = {}

        for index, num in enumerate(nums):

            if target - num in hash_map:
                return [hash_map[target - num], index]
            else:
                hash_map[num] = index
        return []


if __name__ == "__main__":
    two_sum = TwoSum()
    print(two_sum.find_index([2, 7, 11, 15], 9))
    print(two_sum.find_index([3, 2, 4], 6))
    print(two_sum.find_index([3, 3], 6))