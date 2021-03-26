from typing import List
from collections import defaultdict


class Array:

    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach: Stack
        Time Complexity: O(N + M)
        Space Complexity: O(M + N)
        :param nums1:
        :param nums2:
        :return:
        """

        stack = []
        next_element = defaultdict(lambda: -1)
        # next_element = {}

        for n2 in nums2:
            while stack and n2 > stack[-1]:
                next_element[stack.pop()] = n2
            stack.append(n2)

        """
        while stack:
            next_element[stack.pop()] = -1
        """
        result = []
        for n1 in nums1:
            result.append(next_element[n1])
        return result


if __name__ == "__main__":
    array = Array()
    print(array.next_greater_element(
        [4, 1, 2], [1, 3, 4, 2]
    ))
