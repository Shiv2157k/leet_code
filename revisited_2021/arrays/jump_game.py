from typing import List


class Array:

    def can_jump(self, nums: List[int]) -> bool:
        """
        Approach: Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        max_reach, length = 0, len(nums)
        for i in range(length):
            if nums[i] + i > max_reach:
                max_reach = nums[i] + i
            if max_reach == i:
                break
        return max_reach >= length - 1


if __name__ == "__main__":
    array = Array()
    print(array.can_jump([2, 3, 1, 1, 4]))
    print(array.can_jump([3, 2, 1, 0, 4]))