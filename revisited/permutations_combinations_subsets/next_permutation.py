from typing import List


class Permutation:

    def get_next_permutation(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        left, right = len(nums) - 2, len(nums) - 1

        # find the decreasing element
        while left >= 0  and nums[left] > nums[left + 1]:
            left -= 1

        # if you have reached extreme left i.e., starting index
        # reverse the entire list for next permutation
        if left == -1:
            nums.reverse()
        else:
            # find the element less than decreasing element from left to right
            while right >= left and nums[left] >= nums[right]:
                right -= 1

            # swap the left and right index elements
            nums[left], nums[right] = nums[right], nums[left]

            # reverse the sublist starting from left + 1 to the end of the list
            nums[left + 1:] = nums[left + 1:][::-1]
        return nums


if __name__ == "__main__":
    permutations = Permutation()
    print(permutations.get_next_permutation([3, 2, 1]))
    print(permutations.get_next_permutation([1, 2, 3]))
    print(permutations.get_next_permutation([1, 3, 2]))
    print(permutations.get_next_permutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))