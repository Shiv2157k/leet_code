from typing import List


class SingleNumber:

    def get(self, nums: List[int]) -> int:
        """
        Approach: Bit Manipulation using XOR
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    def get_(self, nums: List[int]) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        from collections import defaultdict
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] += 1
        for num in hash_map:
            if hash_map[num] == 1:
                return num


if __name__ == "__main__":
    single_number = SingleNumber()
    print(single_number.get([2, 2, 9]))
    print(single_number.get_([2, 3, 3]))