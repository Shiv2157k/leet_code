from typing import List


class SortedArray:

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Approach: Re-write the index value
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        position = count = 1
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[position] = nums[idx]
                position += 1
        return nums, position

    def remove_duplicates_(self, nums: List[int]) -> int:
        """
        Approach: Popping out elements
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        count = 1
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx - 1]:
                count += 1
                if count > 2:
                    nums.pop(idx)
                    idx -= 1
            else:
                count = 1
            idx += 1
        return nums, len(nums)


if __name__ == "__main__":
    sorted_array = SortedArray()
    print(sorted_array.remove_duplicates([1, 1, 1, 2, 3, 3, 3, 4, 4, 4]))
    print(sorted_array.remove_duplicates_([1, 1, 1, 2, 3, 3, 3, 4, 4, 4]))
