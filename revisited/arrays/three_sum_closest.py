from typing import List


class ThreeSum:

    def find_closest_(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers Slightly Optimized
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0

        nums.sort()
        length, closest = len(nums), nums[0] + nums[1] + nums[2]
        for idx in range(length - 2):
            left, right = idx + 1, length - 1
            while left < right:
                result = nums[idx] + nums[left] + nums[right]
                if abs(target - result) < abs(target - closest):
                    closest = result

                if result < target:
                    left += 1
                elif result > target:
                    right -= 1
                else:
                    return target
        return closest

    def find_closest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0

        # sort the nums
        nums.sort()
        # initiate min diff to max value
        length, min_diff = len(nums), float("inf")

        # loop through the array
        for idx in range(length):
            left, right = idx + 1, length - 1
            while left < right:
                result = nums[idx] + nums[left] + nums[right]
                if abs(target - result) < abs(target - min_diff):
                    min_diff = target - result
                if result < target:
                    left += 1
                else:
                    right -= 1
            if min_diff == 0:
                break
        return target - min_diff


if __name__ == "__main__":
    three_sum = ThreeSum()
    print(three_sum.find_closest([1, 1, -1, -1, 3], -1))
    print(three_sum.find_closest([1, 1, -1, -1, 3], 2))
    print(three_sum.find_closest_([1, 1, -1, -1, 3], -1))
    print(three_sum.find_closest_([1, 1, -1, -1, 3], 2))