from typing import List


class FirstMissingPositive:

    def _get(self, nums: List[int]) -> int:
        """
        Approach: Index as a hash key.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        # base case
        if 1 not in nums:
            return 1

        size = len(nums)
        if size == 1:
            return 2

        # flip the numbers in the array less the or equal to 0
        # and greater than size to 1
        for index, num in enumerate(nums):
            if num <= 0 or num > size:
                nums[index] = 1

        # hash the values based on index
        # use negative sign as a detector
        # for numbers already present in array
        for index, num in enumerate(nums):
            val = abs(num)

            # hash the index values with negative sign
            if val == size:
                nums[0] = - abs(nums[0])
            else:
                nums[val] = - abs(nums[val])

        # loop through index 1 to size
        # if positive element is found return
        # the index
        for index in range(1, size):
            if nums[index] > 0:
                return index
        # if 1st index value is greater than zero
        # return the size
        if nums[0] > 0:
            return size
        # if not return the last index + 1
        return size + 1


if __name__ == "__main__":
    missing_number = FirstMissingPositive()
    print(missing_number._get([3, 4, -1, -2, 1, 5, 16, 0, 2]))
    print(missing_number._get([1]))
    print(missing_number._get([5]))
    print(missing_number._get([0, 1, 2]))

