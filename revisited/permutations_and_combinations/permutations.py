from typing import List


class Permutations:

    def permutee(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back track
        Time Complexity:
        Space Complexity:
        :param nums:
        :return:
        """
        def back_track(nums: List[int], path: List[int], result: List[List[int]]):
            # base case
            if not nums:
                result.append(path)
            for idx in range(len(nums)):
                back_track(nums[:idx] + nums[idx + 1:], path + [nums[idx]], result)

        result = []
        back_track(nums, [], result)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking
        Time Complexity: O(N!)
        Space Complexity: O(N!)
        :param nums:
        :return:
        """

        def back_track(first: int = 0):
            # base case
            if first == n:
                output.append(nums[:])
            for idx in range(first, n):
                # place ith element first in the nums
                nums[first], nums[idx] = nums[idx], nums[first]
                # proceed to create all permutations which starts from ith integer
                back_track(first + 1)
                # back_track t
                nums[first], nums[idx] = nums[idx], nums[first]

        n = len(nums)
        output = []
        back_track()
        return output


if __name__ == "__main__":
    permutations = Permutations()
    permutationss = Permutations()
    print(permutations.permute([1, 2, 3]))
    print(permutationss.permutee([1, 2, 3]))