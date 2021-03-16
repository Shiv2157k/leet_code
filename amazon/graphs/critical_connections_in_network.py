from typing import List
from collections import defaultdict


class Network:

    graphs = defaultdict(list)
    connection_dict = dict()
    rank = dict()

    def critical_connections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS for cycle detection
        Time Complexity: O(V + E) V -> Number of Vertices, E -> Number of Edges
        Space Complexity: O(E) - sum of space occupied by connection dict, rank,
        graph ds i.e., E + V + (V + E) = O(E)
        :param n:
        :param connections:
        :return:
        """
        self.build_adjaceny_nodes_and_reorder_connections(n, connections)
        result = []
        self.dfs(0, 0)
        for e1, e2 in self.connection_dict:
            result.append((e1, e2))
        return result

    def dfs(self, node: int, discovery_rank: int):

        # base case
        if self.rank[node]:
            return self.rank[node]

        self.rank[node] = discovery_rank
        minimum_rank = discovery_rank + 1

        for neighbor in self.graphs[node]:
            # skip the parent
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            if recursive_rank <= discovery_rank:
                del self.connection_dict[min(neighbor, node), max(neighbor, node)]
            # update the minimum rank
            minimum_rank = min(minimum_rank, recursive_rank)
        return minimum_rank

    def build_adjaceny_nodes_and_reorder_connections(self, n: int, connections: List[List[int]]):

        # re-initialize for every cycle
        self.graphs = defaultdict(list)
        self.rank = dict()
        self.connection_dict = dict()

        for node in range(n):
            self.rank[node] = None

        for e1, e2 in connections:
            self.graphs[e1].append(e2)
            self.graphs[e2].append(e1)

            self.connection_dict[min(e1, e2), max(e1, e2)] = 1


if __name__ == "__main__":
    network = Network()
    nw = Network()
    print(nw.critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
    print(network.critical_connections(5, [[0, 1], [1, 2], [2, 0], [1, 3], [2, 4]]))