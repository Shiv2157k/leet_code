from typing import List


class Array:

    def permute_(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking (Swapping)
        Time Complexity: O(∑ k=1,N P(N,k))
        Space Complexity: O(N!)
        :param nums:
        :return:
        """

        def back_track(nums: List[int], path: List[int], permutations: List[List[int]]):
            # base case
            if not nums:
                permutations.append(path)
            for i in range(len(nums)):
                back_track(nums[:i] + nums[i + 1:], path + [nums[i]], permutations)

        permutations = []
        back_track(nums, [], permutations)
        return permutations

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking (Swapping)
        Time Complexity: O(∑ k=1,N P(N,k))
        Space Complexity: O(N!)
        :param nums:
        :return:
        """

        def back_track(first: int = 0):
            # base case
            # if all integers are used up
            if first == n:
                permutations.append(nums[:])
            for i in range(first, n):
                # place i-th integer first in current permutation
                nums[i], nums[first] = nums[first], nums[i]
                # use next integers to complete the next permutation
                back_track(first + 1)
                # back track
                nums[i], nums[first] = nums[first], nums[i]

        permutations = []
        n = len(nums)
        back_track()
        return permutations


if __name__ == "__main__":
    array = Array()
    print(array.permute([1, 2, 3]))
    print(array.permute_([1, 2, 3]))
