from typing import List


class Colors:

    def sort_in_order(self, nums: List[int]) -> List[int]:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        left, right = 0, len(nums) - 1
        curr_idx = 0

        while curr_idx <= right:

            if nums[curr_idx] == 0:
                nums[left], nums[curr_idx] = nums[curr_idx], nums[left]
                left += 1
                curr_idx += 1
            elif nums[curr_idx] == 2:
                nums[right], nums[curr_idx] = nums[curr_idx], nums[right]
                right -= 1
            else:
                curr_idx += 1
        return nums


if __name__ == "__main__":
    colors = Colors()
    print(colors.sort_in_order([0, 2, 1, 2, 0, 0, 1]))
