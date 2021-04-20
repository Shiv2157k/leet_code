from typing import List


class Permutation:

    def next_permutation(self, nums: List[int]) -> List[int]:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        left, right = len(nums) - 2, len(nums) - 1

        # find the index that breaks the order from right side
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # if we have reached the initial index
        # just reverse the whole array
        if left == -1:
            nums.reverse()
        else:
            # find the element closest to left index in which is greater
            while right >= left and nums[left] >= nums[right]:
                right -= 1
            # swap the left and right index values
            nums[left], nums[right] = nums[right], nums[left]
            # reverse elements right to the left index
            nums[left + 1:] = nums[left + 1:][::-1]
        return nums


if __name__ == "__main__":
    permutation = Permutation()
    print(permutation.next_permutation([1, 2, 3]))
    print(permutation.next_permutation([3, 2, 1]))
    print(permutation.next_permutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))