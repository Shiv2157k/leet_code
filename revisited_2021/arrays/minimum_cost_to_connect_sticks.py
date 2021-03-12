import heapq
from typing import List


class Sticks:

    def minimum_cost(self, sticks: List[int]) -> int:
        """
        Approach: Heapq or Priority Queue
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param sticks:
        :return:
        """
        if len(sticks) < 2:
            return 0
        cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            total = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += total
            heapq.heappush(sticks, total)
        return cost


if __name__ == "__main__":
    pullalu = Sticks()
    print(pullalu.minimum_cost([2, 4, 3]))
    print(pullalu.minimum_cost([2, 3]))
    print(pullalu.minimum_cost([9]))