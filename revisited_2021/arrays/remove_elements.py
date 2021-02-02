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
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == "__main__":
    elements = Elements()
    print(elements.remove([1, 1, 2, 3, 3, 1], 1))