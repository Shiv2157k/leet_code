from typing import List


class Triangle:

    def valid_triangle_number_(self, nums: List[int]) -> int:
        """
        Approach: Linear Scan
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        nums.sort()
        result = 0

        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] != 0: # for case [0, 1, 0, 1]
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    result += (k - j - 1)
        return result

    def valid_triangle_number(self, nums: List[int]) -> int:
        """
        Approach: Linear Scan
        Time Complexity: O(N^2 log N)
        Space Complexity: O(log N)
        :param nums:
        :return:
        """

        nums.sort()
        result = 0
        n = len(nums)

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == "__main__":
    triangle = Triangle()
    print(triangle.valid_triangle_number([2, 2, 3, 4]))
    print(triangle.valid_triangle_number_([2, 2, 3, 4]))