from typing import List


class Subsets:

    def get_all__(self, nums: int) -> List[List[int]]:
        """
        Approach: Back tracking
        Time Complexity: O(N2^N)
        Space Complexity: O(N2^N)
        :param nums:
        :return:
        """
        n = len(nums)
        res = []
        nums.sort()

        def back_track(nums, index, path, res):
            # base case
            res.append(path)
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                back_track(nums, i + 1, path + [nums[i]], res)

        back_track(nums, 0, [], res)
        return res

    def get_all_(self, nums: int) -> List[List[int]]:
        """
        Approach: Lexographic Binary Sorted
        Time Complexity: O(N2^N)
        Space Complexity: O(N2^N)
        :param nums:
        :return:
        """
        n = len(nums)
        # make sure all duplications are aligned
        nums.sort()
        output = []
        for i in range(1 << n, 1 << n + 1):
            bitmask = bin(i)[3:]
            sub = []
            for idx in range(n):
                if bitmask[idx] == "1":
                    sub.append(nums[idx])
            if sub not in output:
                output.append(sub)
        return output

    def get_all(self, nums: int) -> List[List[int]]:
        """
        Approach: Cascading
        Time Complexity: O(N2^N)
        Space Complexity: O(N2^N)
        :param nums:
        :return:
        """
        output = [[]]
        nums.sort()
        for num in nums:
            output += [[num] + curr for curr in output if [num]+curr not in output]
        return output


if __name__ == "__main__":
    subsets = Subsets()
    print(subsets.get_all([1, 2, 2]))
    print(subsets.get_all_([1, 2, 2]))
    print(subsets.get_all__([1, 2, 2]))
