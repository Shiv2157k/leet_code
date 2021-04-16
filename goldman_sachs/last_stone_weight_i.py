import heapq
from typing import List


class LastStone:

    def available(self, stones: List[int]) -> int:
        """
        Approach: Heap
        Time Complexity: O(N log N)
        Space Complexity: O(N) or O(log N)
        :param stones:
        :return:
        """

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)

            if stone_1 != stone_2:
                heapq.heappush(stones, (stone_2 - stone_1))
        return -heapq.heappop(stones) if stones else 0


if __name__ == "__main__":
    last_stone = LastStone()
    print(last_stone.available([2, 7, 4, 1, 8, 1]))
