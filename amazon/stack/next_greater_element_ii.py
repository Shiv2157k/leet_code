from typing import List


class Array:

    def next_greater_elements(self, nums: List[int]) -> List[int]:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        stack = []
        nge = [-1] * len(nums)

        for _ in range(2):
            for i, num in enumerate(nums):
                while stack and num > nums[stack[-1]]:
                    nge[stack.pop()] = num
                stack.append(i)
        return nge


if __name__ == "__main__":
    array = Array()
    print(array.next_greater_elements(
        [3, 8, 4, 1, 2]
    ))
    print(array.next_greater_elements(
        [1, 2, 1]
    ))