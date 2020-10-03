from typing import List


class Sequence:

    def get_longest_sequence(self, nums: List[int]) -> int:
        """
        Approach: Hash set and intelligence sequence building.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        longest_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


    def get_longest_sequence_(self, nums: List[int]) -> int:
        """
        Approach: Sorting
        Time Complexity: O( Log N)
        Space Complexity: O(N) or O(1)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        nums.sort()
        longest_streak = current_streak = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)

    def get_longest_sequence__(self, nums: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak


if __name__ == "__main__":
    seq = Sequence()
    print(seq.get_longest_sequence__([100, 4, 200, 2, 3, 1, 2]))
    print(seq.get_longest_sequence_([100, 4, 200, 2, 3, 1, 2]))
    print(seq.get_longest_sequence([100, 4, 200, 2, 3, 1, 2]))