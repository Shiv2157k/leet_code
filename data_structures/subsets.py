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
        n = len(nums)
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


if __name__ == "__main__":
    subset = Subset()
    print(subset.get_subsets([1, 2, 3]))
    print(subset.get_subsets_([1, 2, 3]))
    print(subset.get_subsets__([1, 2, 3]))