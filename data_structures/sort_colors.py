from typing import List


class Colors:

    def sort_colors(self, nums: List[int]) -> List[int]:
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
                nums[curr], nums[left] = nums[left], nums[curr]
                curr += 1
                left += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1
        return nums


if __name__ == "__main__":
    colors = Colors()
    print(colors.sort_colors([0, 2, 1, 0, 2, 1]))
    print(colors.sort_colors([2, 2, 0, 0, 1, 1]))
    print(colors.sort_colors([1, 1, 0, 0, 2, 2]))
    print((colors.sort_colors([0, 0, 2, 2, 1, 1])))
    print(colors.sort_colors([0, 1, 2, 0, 1, 2]))
    print(colors.sort_colors([2, 1, 0, 2, 1, 0]))
    print(colors.sort_colors([1, 2, 0, 1, 2, 0]))
    print(colors.sort_colors([0, 1, 2, 0, 2, 0, 1, 2]))
