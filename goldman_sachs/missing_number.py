from typing import List


class Numbers:

    def get_missing(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        missing_number = len(nums)
        for i, num in enumerate(nums):
            missing_number = missing_number ^ i ^ num
        return missing_number