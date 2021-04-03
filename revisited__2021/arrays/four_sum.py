from typing import List


class Array:

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach: Two Pointers
        Time Complexity: O(N^k - 1) or O(N^3)
        Space Complexity: O(N)
        :param nums:
        :param target:
        :return:
        """
        if len(nums) < 3:
            return []
        nums.sort()
        length = len(nums)
        output = []

        for idx in range(length - 3):
            first = nums[idx]
            if idx > 0 and first == nums[idx - 1]:
                continue
            if first * 4 > target:
                break
            for next_idx in range(idx + 1, length - 2):
                second = nums[next_idx]
                if next_idx > idx + 1 and second == nums[next_idx - 1]:
                    continue
                if second * 3 > target - first:
                    break

                left = next_idx + 1
                right = length - 1
                while left < right:
                    result = first + second + nums[left] + nums[right]
                    if result == target:
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
    array = Array()
    print(array.four_sum([1, 0, -1, 0, -2, 2], 0))