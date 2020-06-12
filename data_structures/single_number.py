from typing import List
from collections import defaultdict


class Single:

    def get_number(self, nums: List[int]) -> int:
        """
        Approach: Using Hash Map.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param nums:
        :return:
        """
        mapper = defaultdict(int)
        for num in nums:
            mapper[num] += 1
        for num in mapper:
            if mapper[num] == 1:
                return num

    def get_number_(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation.
        a xor 0 = a
        a xor a = 0
        a xor b xor a = b
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    single = Single()
    print(single.get_number_([4, 5, 6, 4, 5, 6, 9, 10, 10, 11, 11]))
    print(single.get_number([4, 5, 6, 4, 5, 6, 9, 10, 10, 11, 11]))
