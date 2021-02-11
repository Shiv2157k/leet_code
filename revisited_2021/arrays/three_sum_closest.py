from typing import List


class Array:

    def get_three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N^2)
        Space Complexity: O(log N) to O(N)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0

        nums.sort()
        length, closest = len(nums), nums[0] + nums[1] + nums[2]
        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                curr_target = nums[i] + nums[left] + nums[right]
                if abs(target - curr_target) < abs(target - closest):
                    closest = curr_target
                if curr_target < target:
                    left += 1
                elif curr_target > target:
                    right -= 1
                else:
                    return curr_target
        return closest


if __name__ == "__main__":
    array = Array()
    print(array.get_three_sum_closest([-1, 2, 1, -4], 1))