from typing import List


class Array:

    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking
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
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                back_track(nums[:i] + nums[i + 1:], path + [nums[i]], permutations)
        permutations = []
        nums.sort()
        back_track(nums, [], permutations)
        return permutations


if __name__ == "__main__":
    array = Array()
    print(array.permute_unique([1, 1, 2]))