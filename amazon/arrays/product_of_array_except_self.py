from typing import List


class Array:

    def product_except_itself(self, nums: List[int]) -> List[int]:
        """
        Approach: Single Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        output = [0] * n
        output[0] = 1
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        product = 1
        for i in range(n - 1, -1, -1):

            output[i] = output[i] * product
            product *= nums[i]
        return output

    def product_except_itself_(self, nums: List[int]) -> List[int]:
        """
        Approach: Two Pass
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        n = len(nums)
        left, right = [0] * n, [0] * n
        left[0], right[n - 1] = 1, 1

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        ans = [0] * n
        ans[0] = 1
        for i in range(n):
            ans[i] = left[i] * right[i]
        return ans


if __name__ == "__main__":
    arr = Array()
    print(arr.product_except_itself(
        [1, 2, 3, 4]
    ))
    print(arr.product_except_itself_(
        [1, 2, 3, 4]
    ))
