from typing import List


class SortedArray:

    def remove_duplciates(self, nums: List[int]) -> int:
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
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == "__main__":
    array = SortedArray()
    print(array.remove_duplciates([1, 1, 2]))