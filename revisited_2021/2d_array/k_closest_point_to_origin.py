import heapq
from typing import List


class Points:

    def k_closes_points_to_origin(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time Complexity: O(N log K)
        Space Complexity: O(N)
        :param points:
        :param k:
        :return:
        """
        heap = []
        for x, y in points:
            if len(heap) < k:
                heapq.heappush(heap, [-(x*x + y*y), [x, y]])
            else:
                heapq.heappushpop(heap, [-(x*x+y*y), [x, y]])
        return [pair for _, pair in heap]


if __name__ == "__main__":
    p = Points()
    print(p.k_closes_points_to_origin([[1, 3], [-2, 2]], 1))