from typing import List


class PlusOne:

    def get_solution(self, nums: List[int]) -> List[int]:
        """
        Approach: School Book Addition with carrry.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        n = len(nums)
        # move along the input array starting from the end.
        for i in range(n - 1, -1, -1):
            # set all the nines at end of the array to zero.
            if nums[i] == 9:
                nums[i] = 0
            # here we have the right most non nine.
            else:
                # increase the right most non nine by 1.
                nums[i] += 1
                # addition is done.
                return nums
        # if all the digits are nines we reach here.
        return [1] + nums


if __name__ == "__main__":
    plus_one = PlusOne()
    print(plus_one.get_solution([1, 2, 3]))
    print(plus_one.get_solution([1, 2, 9]))
    print(plus_one.get_solution([9, 8, 9]))