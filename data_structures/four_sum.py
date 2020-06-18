from typing import List, Set


class FourSum:

    def get_list(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        length, output = len(nums), []

        for i in range(length - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                break

            for j in range(i + 1, length - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] * 3 > target - nums[i]:
                    break

                left, right = j + 1, length - 1
                while left < right:
                    res = nums[i] + nums[j] + nums[left] + nums[right]
                    if res == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif res < target:
                        left += 1
                    else:
                        right -= 1
        return output

    def get_set(self, nums: List[int], target: int) -> Set[Set[int]]:
        """
        Approach: Using Hash Set
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        length = len(nums)

        reference, output, last = {nums[i]: i for i in range(length)}, set(), nums[-1]

        for i in range(length - 3):
            first = nums[i]
            if first + 3 * last < target:
                continue
            if first * 4 > target:
                break
            for j in range(i + 1, length - 2):
                second = nums[j]
                if first + second + 2 * last < target:
                    continue
                if second * 3 > target - first:
                    break
                for k in range(j + 1, length - 1):
                    third = nums[k]
                    fourth = target - (first + second + third)

                    if fourth > last:
                        continue
                    if fourth < third:
                        break
                    if fourth in reference and reference[fourth] > k:
                        output.add((first, second, third, fourth))
        return output


if __name__ == "__main__":

    four_sum = FourSum()
    print(four_sum.get_set([1, 0, -1, 0, -2, 2], 0))
    print(four_sum.get_list([1, 0, -1, 0, -2, 2], 0))
