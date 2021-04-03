from typing import List


class Array:

    def three_sum_closest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N^2)
        Space Complexity: O(log N) to O(N)
        :param nums:
        :param target
        :return:
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        length = len(nums)

        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if abs(target - result) < abs(target - closest):
                    closest = result
                if result < target:
                    left += 1
                elif result > target:
                    right -= 1
                else:
                    return target
        return closest


if __name__ == "__main__":
    array = Array()
    print(array.three_sum_closest(
        [-1, 2, 1, -4], 1
    ))