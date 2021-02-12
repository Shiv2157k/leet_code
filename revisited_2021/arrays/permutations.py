from typing import List


class Permutation:

    def next(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        left, right = len(nums) - 2, len(nums) - 1

        # decrement until the ascending order breaks
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # if reached the end
        # reverse everything
        if left == -1:
            nums.reverse()
        else:
            # find the closest ascending element
            while right >= left and nums[left] >= nums[right]:
                right -= 1
            # swap
            nums[left], nums[right] = nums[right], nums[left]
            # reverse the elements next to left
            nums[left + 1:] = nums[left + 1:][::-1]
        return nums


if __name__ == "__main__":
    permutation = Permutation()
    print(permutation.next([1, 2, 3]))
    print(permutation.next([3, 2, 1]))
    print(permutation.next([1, 3, 2]))
    print(permutation.next([1, 3, 2, 4]))
