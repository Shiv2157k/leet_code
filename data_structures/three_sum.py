from typing import List, Set


class ThreeSum:

    def get_list(self, nums: List[int]) -> Set[Set[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        :param nums:
        :return:
        """
        if not nums:
            return []
        nums.sort()
        length = len(nums)
        reference, last, output = {nums[i]: i for i in range(length)}, nums[-1], set()
        for i in range(length - 2):
            first = nums[i]
            if first + (2 * last) < 0:
                continue
            if first * 3 > 0:
                break
            for j in range(i + 1, length - 1):
                second = nums[j]
                if first + second + last < 0:
                    continue
                if first + (2 * second) > 0:
                    break
                third = 0 - (first + second)
                if third > last:
                    continue
                elif third < second:
                    break
                elif third in reference and reference[third] > j:
                    output.add((first, second, third))
        return output

    def get_list_(self, nums: List[int]) -> List[List]:
        """
        Approach: Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        :param nums:
        :return:
        """
        if not nums:
            return []
        nums.sort()
        length, output = len(nums), []
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    right -= 1
        return output

    def get_closest(self, nums: List[int], target: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        :param nums:
        :param target:
        :return:
        """

        if not nums:
            return 0
        length, closest = len(nums), nums[0] + nums[1] + nums[2]
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
    three_sum = ThreeSum()
    print(three_sum.get_list_([-1, 0, 1, 2, -1, -4]))
    print(three_sum.get_list([-1, 0, 1, 2, -1, -4]))
    print(three_sum.get_closest([-1, 2, 1, -4], 1))







