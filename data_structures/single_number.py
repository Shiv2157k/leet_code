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

    def number_ii(self, nums: List[int]) -> int:
        """
        Approach: Using hashset
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def number__ii(self, nums: List[int]) -> int:
        """
        Approach: Using Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        from collections import Counter
        hashmap = Counter(nums)
        for num in hashmap.keys():
            if hashmap[num] == 1:
                return num

    def number___ii(self, nums: List[int]) -> int:
        """
        Approach: Bit-wise Operator
        Time Complexity: O(N)
        Space Complexity: O(1)
        Formulae:
        l' = ~h & (l ^ i)
        h' = ~l' & (h ^ i)
        :param nums:
        :return:
        """
        once = twice = 0
        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)
        return once


if __name__ == "__main__":
    single = Single()
    print(single.get_number_([4, 5, 6, 4, 5, 6, 9, 10, 10, 11, 11]))
    print(single.get_number([4, 5, 6, 4, 5, 6, 9, 10, 10, 11, 11]))
    print(single.get_number_([4, 1, 2, 1, 2]))
    print(single.number___ii([1, 1, 1, 5, 5, 5, 99]))
    print(single.number__ii([1, 1, 1, 5, 5, 5, 99]))
    print(single.number_ii([1, 1, 1, 5, 5, 5, 99]))
