from typing import List


class Subset:

    def get_all_via_bit_manipulation(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Lexicographic (Binary Sorted) subsets
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        n = len(nums)
        nums.sort()
        subset = []

        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            sub = []
            for j in range(n):
                if bitmask[j] == "1":
                    sub.append(nums[j])
            if sub not in subset:
                subset.append(sub)
        return subset

    def get_all(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back Tracking.
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        def back_track(nums, index, path, result):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                back_track(nums, i + 1, path + [nums[i]], res)

        nums.sort()
        res = []
        back_track(nums, 0, [], res)
        return res


if __name__ == "__main__":
    subset = Subset()
    subset_1 = Subset()
    print(subset.get_all([1, 2, 2]))
    print(subset_1.get_all_via_bit_manipulation([1, 2, 2]))