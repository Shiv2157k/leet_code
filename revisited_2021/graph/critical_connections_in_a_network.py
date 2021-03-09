from typing import List
from collections import defaultdict


class Network:
    # to keep track of ranks
    ranks = dict()
    # to keep track of each node adjacency
    graphs = defaultdict(list)
    # for re-organizing the connections in a proper way
    connection_dicts = dict()

    def get_critical_connections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS for cycle detection
        Time Complexity: O(V + E)
        Space Complexity: O(E)
        :param n:
        :param connections:
        :return:
        """
        self.build_graph_rank_and_adjust_connections(n, connections)
        # stars from node 0 with discovery rank starting with 0
        self.dfs(0, 0)
        critical_connections = []

        for e1, e2 in self.connection_dicts:
            critical_connections.append((e1, e2))
        return critical_connections

    def dfs(self, node: int, discovery_rank: int) -> int:
        # base case
        # if rank of a node already exists
        # means it is already visited
        # just return the node rank
        if self.ranks[node]:
            return self.ranks[node]
        # update the node rank with discovery rank
        self.ranks[node] = discovery_rank

        # min rank to keep track if this is a cycle
        # max we have seen so far
        min_rank = discovery_rank + 1
        # iterate through each graph nodes to recognize cycles
        for neighbor in self.graphs[node]:
            # skip the parent
            if self.ranks[neighbor] and self.ranks[neighbor] == discovery_rank - 1:
                continue
            # Apply the recursion
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Step 1: delete the nodes in the cycle
            if recursive_rank <= discovery_rank:
                del self.connection_dicts[min(neighbor, node), max(neighbor, node)]
            # Step 2: update the min rank
            min_rank = min(recursive_rank, min_rank)
        return min_rank

    def build_graph_rank_and_adjust_connections(self, n: int, connections: List[List[int]]):
        """
        :param n:
        :param connections:
        :return:
        """

        # set the rank of all nodes to None
        for node in range(n):
            self.ranks[node] = None

        # build the graph and adjust connections
        for edge in connections:
            e1, e2 = edge[0], edge[1]
            self.graphs[e1].append(e2)
            self.graphs[e2].append(e1)
            self.connection_dicts[min(e1, e2), max(e1, e2)] = 1


if __name__ == "__main__":
    network = Network()
    nw = Network()
    print(nw.get_critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
    print(network.get_critical_connections(5, [[0, 1], [1, 2], [2, 0], [1, 3], [2, 4]]))
