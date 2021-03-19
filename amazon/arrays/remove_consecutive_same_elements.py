from typing import List


class Array:

    def remove_consecutive_same_element(self, nums: List[int]) -> List:
        """
        Approach: Stack DS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        stack = []
        for num in nums:
            stack.append(num)
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack = stack[:-2]
        return stack


if __name__ == "__main__":
    array = Array()
    print(array.remove_consecutive_same_element(
        [1, 0, 0, 0, 0, 8, 8, 8, 8, 7, 7, 7, 9, 9, 9]
    ))
    print(array.remove_consecutive_same_element(
        [0, 9, 9, 9, 7, 7, 9, 6, 6, 8]
    ))
    print(array.remove_consecutive_same_element(
        [0, 9, 9, 9, 7, 7, 6, 6, 8]
    ))
