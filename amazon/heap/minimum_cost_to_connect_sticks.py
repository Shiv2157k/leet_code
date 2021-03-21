import heapq

from typing import List


class Sticks:

    def minimum_cost_to_connect(self, sticks: List[int]) -> int:
        """
        Approach: Heap
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param sticks:
        :return:
        """
        if len(sticks) < 2:
            return 0
        min_cost = 0

        heapq.heapify(sticks)

        while len(sticks) > 1:
            total = heapq.heappop(sticks) + heapq.heappop(sticks)
            min_cost += total
            heapq.heappush(sticks, total)
        return min_cost


if __name__ == "__main__":
    S = Sticks()
    print(S.minimum_cost_to_connect(
        [2, 4, 3]
    ))
    print(S.minimum_cost_to_connect(
        [1, 8, 3, 5]
    ))
    print(S.minimum_cost_to_connect(
        [5]
    ))
