from typing import List


class PositiveInteger:

    def get_first_missing(self, nums: List[int]) -> int:
        """
        Approach: Using index hash
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """

        # base case
        # if there is no 1 in given list
        # return 1
        if 1 not in nums:
            return 1

        size = len(nums)

        # if size is 1 then return 2
        if size == 1:
            return 2

        # mark all the numbers less than 0 and
        # all the numbers greater than size of list
        # to 1
        for idx, num in enumerate(nums):
            if num > size or num <= 0:
                nums[idx] = 1

        # mark all the value index to negative
        # Use index as hash key and number sign as a presence detector.
        for idx, num in enumerate(nums):
            val = abs(num)

            # if you meet number val in array - change the sign of
            # val-th element
            # do it only once

            if val == size:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        # Now the index of first positive number is equal to
        # first missing positive.
        for idx in range(1, size):
            if nums[idx] > 0:
                return idx
        if nums[0] > 0:
            return size
        return size + 1



