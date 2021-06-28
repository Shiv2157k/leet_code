from typing import List


class Flights:

    def __init__(self):
        self.adj_matrix = None
        self.memo = {}

    def get_shortest_flight(self, node: int, stops: int, dest: int, n: int):

        # base cases
        if node == dest:
            return 0
        if stops < 0:
            return float("inf")

        # if it is in the cache
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]

        # initialize the ans to infinity
        ans = float("inf")
        # apply the recursion
        for neighbor in range(n):
            # check if there is a flight for
            # (node, neighbor) combination
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.get_shortest_flight(neighbor, stops - 1, dest, n) + self.adj_matrix[node][neighbor])

        self.memo[(node, stops)] = ans
        return ans

    def get_cheapest_flight_within_k_stops(self, n: int, flights: List[List[int]], src: int, dest: int, k: int):
        """
        Approach: Recursion with Memoization
        Time Complexity: O(V^2 * k)
        Space Complexity: O(V * K + V^2)
        :param n:
        :param flights:
        :param src:
        :param dest:
        :param k:
        :return:
        """
        # initialize adjaceny matrix and dp
        self.adj_matrix = [[0] * n for _ in range(n)]
        for source, destination, cost in flights:
            self.adj_matrix[source][destination] = cost
        self.memo = {}

        result = self.get_shortest_flight(src, k, dest, n)

        return -1 if result == float("inf") else result


if __name__ == "__main__":
    f = Flights()
    print(f.get_cheapest_flight_within_k_stops(
        5,
        [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]],
        2,
        1,
        1,
    ))
    print(f.get_cheapest_flight_within_k_stops(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dest=2, k=1
    ))
    print(f.get_cheapest_flight_within_k_stops(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dest=2, k=0
    ))
