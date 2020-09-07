from typing import List


class SingleNumber:

    def get_using_set(self, nums: List[int]) -> int:
        """
        Approach: Using Set
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2

    def get_using_hashmap(self, nums: List[int]) -> int:
        """
        Approach: Using Hashmap
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        from collections import Counter
        hashmap = Counter(nums)
        for num in hashmap:
            if hashmap[num] == 1:
                return num

    def get_using_bitwise_operator(self, nums: List[int]) -> int:
        """
        Two repetitions can be fetched using xor.
        Three repetitions formulae:
        use not, and, xor operations
        approach: by drawing truth table for 00 -> 01 -> 10 -> 00
                  l' = ~h & (l ^ i)
                  h' = ~l' & (h ^ i)
        Time Complexity: O(N)
        Space Cmplexity: O(1)
        :param nums:
        :return:
        """
        once = twice = 0
        for num in nums:
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)
        return once


if __name__ == "__main__":
    single_number = SingleNumber()
    print(single_number.get_using_set([2, 3, 2, 2]))
    print(single_number.get_using_hashmap([2, 3, 2, 2]))
    print(single_number.get_using_bitwise_operator([2, 3, 2, 2]))
    print(single_number.get_using_set([0, 1, 0, 1, 0, 1, 99]))
    print(single_number.get_using_hashmap([0, 1, 0, 1, 0, 1, 99]))
    print(single_number.get_using_bitwise_operator([0, 1, 0, 1, 0, 1, 99]))

