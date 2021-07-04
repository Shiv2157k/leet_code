from typing import List
from collections import deque


class AllOnes:

    def min_swaps_to_group_(self, data: List[int]) -> int:
        """
        Approach: Sliding Window (Deque)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param data:
        :return:
        """

        total_ones = sum(data)
        max_ones = count_ones = 0

        q = deque()

        for i in range(len(data)):
            q.append(data[i])
            count_ones += data[i]

            if len(q) > total_ones:
                count_ones -= q.popleft()
            max_ones = max(max_ones, count_ones)
        return total_ones - max_ones

    def min_swaps_to_group(self, data: List[int]) -> int:
        """
        Approach: Sliding Window
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param data:
        :return:
        """

        total_ones = sum(data)
        max_ones = count_ones = 0
        left = right = 0

        while right < len(data):
            count_ones += data[right]
            right += 1

            if right - left > total_ones:
                count_ones -= data[left]
                left += 1
            max_ones = max(max_ones, count_ones)
        return total_ones - max_ones


if __name__ == "__main__":
    all_ones = AllOnes()
    print(all_ones.min_swaps_to_group([0, 1, 0, 1, 0]))
    print(all_ones.min_swaps_to_group([0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]))
    print(all_ones.min_swaps_to_group([0, 0, 1, 0, 0]))
    print(all_ones.min_swaps_to_group_([0, 1, 0, 1, 0]))
    print(all_ones.min_swaps_to_group_([0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]))
    print(all_ones.min_swaps_to_group_([0, 1, 0, 0]))