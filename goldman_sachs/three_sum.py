from typing import List


class Array:

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        nums.sort()
        length = len(nums)
        result = []

        for i in range(length - 2):
            left = i + 1
            right = length - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif target > 0:
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == "__main__":

    array = Array()
    print(array.three_sum([-1, 0, 1, 2, -1, -4]))
    print(array.three_sum([0]))