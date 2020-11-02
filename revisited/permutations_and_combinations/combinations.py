from typing import List


class Combination:

    def get_all(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Lexographic Binary Sorted Combinations
        Time Complexity: O (k C(k, n))
        Space Complexity: O (C(k, n))
        :param n:
        :param k:
        :return:
        """
        # generate numbers from 1 to k with n + 1 as sentinel
        nums = [i for i in range(1, k + 1)]
        # sentinel
        nums.append(n + 1)
        left, output = 0, []
        # loop through
        while left < k:
            # add the current combination
            output.append(nums[:k])
            # increase first nums[0] by 1
            # if nums[left] + 1 != nums[left + 1]
            left = 0
            while left < k and nums[left] + 1 == nums[left + 1]:
                nums[left] = left + 1
                left += 1
            nums[left] += 1
        return output

    def get_all_(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        Time Complexity: O (k C(k, n))
        Space Complexity: O (C(k, n))
        :param n:
        :param k:
        :return:
        """

        def back_track(first=1, combination=[]):
            # base case
            if len(combination) == k:
                output.append(combination[:])
            for num in range(first, n + 1):
                # add the number
                combination.append(num)
                # move to the next combination
                back_track(num + 1, combination)
                # back track
                combination.pop()

        output = []
        back_track()
        return output


if __name__ == "__main__":
    combinations = Combination()
    comb = Combination()
    print(comb.get_all(4, 2))
    print(combinations.get_all_(4, 2))