from typing import List


class TwoSum:

    def get_two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity O(N)
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