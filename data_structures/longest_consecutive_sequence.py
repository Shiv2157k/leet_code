from typing import List


class Sequence:

    def find_longest_consecutive(self, nums: List[int]) -> int:
        """
        Approach: Hash Set and Intelligence Sequence Building
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param nums:
        :return:
        """
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

    def find_longest_consecutive_(self, nums: List[int]) -> int:
        """
        Approach: Sorting
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        longest_streak = current_streak = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)

    def find_longest_consecutive__(self, nums: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(n^3)
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
    sequence = Sequence()
    print(sequence.find_longest_consecutive__([100, 200, 3, 4, 2, 1]))
    print(sequence.find_longest_consecutive_([100, 200, 3, 4, 2, 1]))