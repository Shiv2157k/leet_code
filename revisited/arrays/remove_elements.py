from typing import List


class Elements:

    def remove(self, nums: List[int], val: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :param val:
        :return:
        """
        length = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[length] = nums[index]
                length += 1
        return length

    def remove_(self, nums: List[int], val: int) -> int:
        """
        Approach: Two Pointers when elements to be removed are rare.
        :param nums:
        :param val:
        :return:
        """
        if not nums:
            return 0
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right


if __name__ == "__main__":
    elements = Elements()
    print(elements.remove([3, 2, 2, 3], 3))
    print(elements.remove_([3, 2, 2, 3], 3))
    print(elements.remove([3, 2, 2, 3], 2))
    print(elements.remove_([3, 2, 2, 1, 3], 2))