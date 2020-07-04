from typing import List


class Subset:

    def get_subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Cascading
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n * 2^n)
        :param nums:
        :return:
        """
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    def get_subsets_(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n * 2^n)
        :param nums:
        :return:
        """
        def back_track(left=0, curr=[]):
            # base case
            if len(curr) == k:
                output.append(curr[:])
            for i in range(left, n):
                curr.append(nums[i])
                back_track(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n + 1):
            back_track()
        return output

    def get_subsets__(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Lexographic (Binary Sorted) subsets
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        n = len(nums)
        output = []
        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])
        return output

    def get_subsets_II(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Cascading
        Time Complexity: O(N * 2*N)
        Space Complexity: O(N * 2*N)
        :param nums:
        :return:
        """

        nums.sort()
        subsets = [[]]
        for num in nums:
            subsets += [curr + [num] for curr in subsets if curr + [num] not in subsets]
        return subsets

    def get_subsets__II(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Lexographic binary sorting
        Time Complexity: O(N * 2*N)
        Space Complexity: O(N * 2*N)
        :param nums:
        :return:
        """
        n, subsets = len(nums), []
        nums.sort()
        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            sets = []
            for j in range(n):
                if bitmask[j] == "1":
                    sets.append(nums[j])
            if sets not in subsets:
                subsets.append(sets)
        return subsets

    def get_subsets___II(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: DFS (back tracking)
        Time Complexity: O(N * 2*N)
        Space Complexity: O(N * 2*N)
        :param nums:
        :return:
        """

        def back_track(nums, index, path, subsets):
            subsets.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                back_track(nums, i + 1, path + [nums[i]], subsets)

        subsets = []
        nums.sort()
        back_track(nums, 0, [], subsets)
        return subsets


if __name__ == "__main__":
    subset = Subset()
    print(subset.get_subsets([1, 2, 3]))
    print(subset.get_subsets_([1, 2, 3]))
    print(subset.get_subsets__([1, 2, 3]))

    print(subset.get_subsets_II([1, 2, 2]))
    print(subset.get_subsets__II([1, 2, 2]))
    print(subset.get_subsets___II([1, 2, 2]))