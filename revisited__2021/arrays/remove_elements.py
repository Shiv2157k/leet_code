from typing import List


class Array:

    def remove_element(self, nums: List[int], val: int) -> int:
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
    arr = Array()
    print(arr.remove_element([1, 2, 3, 4, 4, 5, 5, 7, 4], 4))
    print(arr.remove_element([1, 2, 3], 2))
    print(arr.remove_element([1, 1, 1], 1))