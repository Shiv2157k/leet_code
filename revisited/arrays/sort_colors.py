from typing import List


class Colors:

    def sort(self, nums: List[int]) -> List[int]:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        left = curr = 0
        right = len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1
        return nums


if __name__ == "__main__":
    colors = Colors()
    print(colors.sort([1, 0, 1, 0, 2, 2]))
    print(colors.sort([2, 0, 1, 2, 2, 0, 0, 1, 1]))
    print(colors.sort([2, 1, 0]))