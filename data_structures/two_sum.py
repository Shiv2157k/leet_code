from typing import List


class TwoSum:

    def two_sum(self, nums: List[int], target: int) -> int:
        """

        :param nums:
        :param target:
        :return:
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            else:
                lookup[num] = i
        return []


if __name__ == "__main__":
    res = TwoSum()
    print(res.two_sum([2, 7, 6, 8, 5], 7))