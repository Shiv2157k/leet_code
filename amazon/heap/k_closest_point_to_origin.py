import heapq
from typing import List


class Points:

    def k_closest_to_origin(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Approach: Heap
        Time Complexity: O(N log K)
        Space Complexity:O(N)
        :param points:
        :param k:
        :return:
        """
        heap = []
        for x, y in points:
            if len(heap) < k:
                heapq.heappush(heap, (-(x * x + y * y), (x, y)))
            else:
                heapq.heappushpop(heap, (-(x * x + y * y), (x, y)))
        return [pair for value, pair in heap]

    # need to try divide and conquer approach


if __name__ == "__main__":
    p = Points()
    print(p.k_closest_to_origin(
        [[3, 3], [5, -1], [-2, 4]], 2
    ))
    print(p.k_closest_to_origin(
        [[1, 3], [-2, 2]], 1
    ))
