from typing import List


class Array:

    def remove_duplicates(self, nums: List[int]) -> int:
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
            if nums[i] != nums[i - 1]:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == "__main__":
    array = Array()
    print(array.remove_duplicates([1, 2, 2]))
    print(array.remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]))