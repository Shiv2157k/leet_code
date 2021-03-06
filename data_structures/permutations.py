from typing import List


class Permutation:

    def get_next(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Pass
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        left, right = len(nums) - 2, len(nums) - 1

        # find the index which breaks the descending order
        # from right side of the list.
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # if the entire list is in descending order
        # permutation starts from the last.
        if left == -1:
            nums.reverse()
            return nums
        else:
            # find the index that contains number closest
            # to left index from the right side.
            while right >= left and nums[left] >= nums[right]:
                right -= 1

            # swap the left and right index.
            nums[left], nums[right] = nums[right], nums[left]
            # reverse the elements right to the left index
            # for the next permutation.
            nums[left + 1:] = nums[left + 1:][::-1]
            return nums

    def get_all_unique_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Back tracking (Recursion)
        :param nums:
        :return:
        """
        # back tracking function
        def back_track(nums, path, unique):

            # base case
            if not nums:
                unique.append(path)

            for i in range(len(nums)):
                # skip if it is a duplicate element.
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                back_track(nums[:i] + nums[i + 1:], path + [nums[i]], unique)

        nums.sort()
        unique = []
        back_track(nums, [], unique)
        return unique

    def get_all_from_distinct(self, nums: List[int]) -> List[List[int]]:

        def back_track(nums, path, permutations):

            if not nums:
                permutations.append(path)
            for i in range(len(nums)):
                back_track(nums[:i] + nums[i + 1:], path + [nums[i]], permutations)

        permutations = []
        back_track(nums, [], permutations)
        return permutations

    def next_permutation(self, k: int, n: int) -> List[int]:
        """
        Approach: Factorial Number System.
        Time Complexity: O(n^2)
        Space Complexity: O(N)
        :param k:
        :param n:
        :return:
        """
        factorials, nums, k, output = [1], ["1"], k - 1, []
        # generate the factorial representation for n.
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))

        # extract the factorial representation to permutation.
        for i in range(n - 1, -1, -1):
            index = k // factorials[i]
            k = k - index * factorials[i]

            output.append(nums[index])
            del nums[index]
        return "".join(output)


if __name__ == "__main__":

    permutation = Permutation()
    print(permutation.get_next([9, 6, 5, 4, 3, 2, 1]))
    print(permutation.get_next([9, 6, 5, 4, 7, 2, 1]))
    print(permutation.get_next([1, 2, 4, 5, 7, 8, 9]))
    print(permutation.get_all_unique_with_duplicates([1, 2, 1]))
    print(permutation.get_all_from_distinct([6, 7, 9]))
    print(permutation.next_permutation(3, 3))