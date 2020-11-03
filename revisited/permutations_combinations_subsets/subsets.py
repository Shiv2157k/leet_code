from typing import List


class Subsets:

    def generated(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Lexographic Binary Sorted
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        n = len(nums)
        output = []
        for i in range(2**n):
            bitmask = bin(i | 1 << n)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])
        return output

    def generate(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Lexographic Binary Sorted
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

    def generate_(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        def back_track(first=0, curr=[]):

            if len(curr) == k:
                output.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                back_track(i + 1, curr)
                curr.pop()

        n = len(nums)
        output = []
        for k in range(n + 1):
            back_track()
        return output

    def generate__(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Cascading
        Time Complexity: O(N * 2^N)
        Space Complexity: O(N * 2^N)
        :param nums:
        :return:
        """
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output


if __name__ == "__main__":
    subsets = Subsets()
    print(subsets.generated([1, 2, 3]))
    print(subsets.generate([1, 2, 3]))
    print(subsets.generate__([1, 2, 3]))
    print(subsets.generate_([1, 2, 3]))