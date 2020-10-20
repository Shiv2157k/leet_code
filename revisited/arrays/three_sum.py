from typing import List


class ThreeSum:

    def get_all_triplets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Using Hashset
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx == 0 or nums[idx - 1] != nums[idx]:
                self.two_sum(nums, idx, res)
        return res

    def two_sum(self, nums: List[int], idx: int, res: List[List[int]]):
        seen = set()
        left = idx + 1
        while left < len(nums):
            complement = -nums[idx] - nums[left]
            if complement in seen:
                res.append([nums[idx], nums[left], complement])
                while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                    left += 1
            seen.add(nums[left])
            left += 1

    def get_operands_(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers without another function
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        nums.sort()
        output = []
        length = len(nums)
        for idx in range(length - 2):

            left = idx + 1
            right = length - 1

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            while left < right:
                target = nums[idx] + nums[left] + nums[right]
                if target == 0:
                    output.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                elif target < 0:
                    left += 1
                else:
                    right -= 1
        return output

    def get_operands(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Two Pointers with two sum II separate function
        Time Complexity: O(N^2)
        Space Complexity: O(log N) to O(N)
        :param nums:
        :return:
        """
        length = len(nums)
        nums.sort()
        output = []
        for idx in range(length):
            if nums[idx] > 0:
                break
            if idx == 0 or nums[idx] != nums[idx - 1]:
                self.two_sum_ii(nums, idx, output)
        return output

    def two_sum_ii(self, nums: List[int], idx: int, output: List[List[int]]):

        left = idx + 1
        right = len(nums) - 1

        while left < right:
            target = nums[idx] + nums[left] + nums[right]
            if target == 0:
                output.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif target < 0:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    three_sum = ThreeSum()
    print(three_sum.get_operands([-1, 0, 1, 2, -1, -4]))
    print(three_sum.get_operands_([-1, 0, 1, 2, -1, -4]))
    print(three_sum.get_all_triplets([-1, 0, 1, 2, -1, -4]))