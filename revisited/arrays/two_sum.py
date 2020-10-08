from typing import List


class TwoSum:

    def get_indices(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: One Pass Hash table
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        reference = {}
        for idx, num in enumerate(nums):
            if target - num in reference:
                return [reference[target - num], idx]
            else:
                reference[num] = idx
        return []


if __name__ == "__main__":
    two_sum = TwoSum()
    print(two_sum.get_indices([2, 7, 11, 15], 26))
    print(two_sum.get_indices([3, 2, 4], 6))
    print(two_sum.get_indices([3, 3], 6))