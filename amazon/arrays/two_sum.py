from typing import List


class TwoSum:

    def get_indexes(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: One Pass Hash Table
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        look_up = {}

        for i, num in enumerate(nums):
            if target - num in look_up:
                return [look_up[target - num], i]
            else:
                look_up[num] = i
        return []


if __name__ == "__main__":
    two_sum = TwoSum()
    print(two_sum.get_indexes(
        [2, 7, 11, 5], 9
    ))
    print(two_sum.get_indexes(
        [2, 7, 11, 5], 16
    ))
    print(two_sum.get_indexes(
        [2, 7, 11, 5], 12
    ))