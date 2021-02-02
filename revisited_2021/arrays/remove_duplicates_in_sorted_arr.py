from typing import List


class SortedArray:

    def remove_duplicates(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        if not nums:
            return 0
        length = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[length] = nums[idx]
                length += 1
        return length


if __name__ == "__main__":
    sorted_arr = SortedArray()
    print(sorted_arr.remove_duplicates([1, 1, 2, 2, 5, 6, 7, 7]))