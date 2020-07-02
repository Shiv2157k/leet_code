from typing import List


class SortedArray:

    def remove_duplicates(self, nums: List) -> int:

        if len(nums) == 0:
            return 0
        len_ = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_

    def remove_duplicates_ii(self, nums: List) -> int:
        """
        Approach: Popping Unwanted Duplicates
        Time Complexity: O(N) worst case is O(N^2)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        pointer = counter = 1
        while pointer < len(nums):
            if nums[pointer] == nums[pointer - 1]:
                counter += 1
                if counter > 2:
                    nums.pop(pointer)
                    pointer -= 1
            else:
                counter = 1
            pointer += 1
        return len(nums)

    def remove_duplicates_ii_(self, nums: List) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        pointer = counter = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                counter += 1
            else:
                counter = 1
            if counter <= 2:
                nums[pointer] = nums[index]
                pointer += 1
        return pointer


if __name__ == "__main__":
    array = SortedArray()
    print(array.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(array.remove_duplicates_ii([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(array.remove_duplicates_ii_([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))