from typing import List


class FourSum:

    def get_unique_quadruplets_(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Hash Set
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        length = len(nums)
        output = set()
        reference = {nums[i]: i for i in range(length)}
        last = nums[-1]

        for idx in range(length - 3):
            first = nums[idx]
            if first + 3 * last < target:
                continue
            if first * 4 > target:
                break
            for next_idx in range(idx + 1, length - 2):
                second = nums[next_idx]
                if first + second + 2 * last < target:
                    continue
                if second * 3 > target - first:
                    break
                for next_next_idx in range(next_idx + 1, length - 1):
                    third = nums[next_next_idx]
                    fourth = target - (first + second + third)
                    if fourth > last:
                        continue
                    if fourth < third:
                        break
                    if fourth in reference and reference[fourth] > next_next_idx:
                        output.add((first, second, third, fourth))
        return output

    def get_unique_quadruplets(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(N^3)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        length = len(nums)
        nums.sort()
        # base case
        if not nums or length < 4:
            return []

        output = []

        for idx in range(length - 3):
            first = nums[idx]
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            if first * 4 > target:
                break
            for next_idx in range(idx + 1, length - 2):
                second = nums[next_idx]
                if next_idx > idx + 1 and nums[next_idx] == nums[next_idx - 1]:
                    continue
                if second * 3 > target - first:
                    break
                left = next_idx + 1
                right = length - 1
                while left < right:
                    result = first + second + nums[left] + nums[right]
                    if target == result:
                        output.append([first, second, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif result < target:
                        left += 1
                    else:
                        right -= 1
        return output


if __name__ == "__main__":
    four_sum = FourSum()
    print(four_sum.get_unique_quadruplets([1, 0, -1, 0, -2, 2], 0))
    print(four_sum.get_unique_quadruplets([1, 0, -1, 0, -2, 2], 1))
    print(four_sum.get_unique_quadruplets_([1, 0, -1, 0, -2, 2], 0))
    print(four_sum.get_unique_quadruplets_([1, 0, -1, 0, -2, 2], 1))