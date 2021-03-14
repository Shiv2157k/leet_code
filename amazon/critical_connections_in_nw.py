from typing import List
from collections import defaultdict


class Network:

    # to keep track of each server node rank
    node_ranks = dict()
    # for building adjacency/  neighbors
    graph = defaultdict(list)
    # re-organizing connections
    connection_dict = dict()

    def critical_connections(self, servers: int, n_connections: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Approach: DFS for cycle detection
        :param servers:
        :param n_connections:
        :param connections:
        :return:
        """
        self.build_adjacency_graph_and_reorganize_connections(servers, connections)
        self.dfs(1, 1)
        result = []
        for e1, e2 in self.connection_dict:
            result.append([e1, e2])
        return result

    def dfs(self, node: int, discovery_rank: int):

        # that means this node is already visited.
        # we simply return rank.
        if self.node_ranks[node]:
            return self.node_ranks[node]
        # update the rank
        self.node_ranks[node] = discovery_rank
        # max rank we have seen so far
        minimum_rank = discovery_rank + 1

        for neighbor in self.graph[node]:

            # if it is a parent simply skip.
            if self.node_ranks[neighbor] and self.node_ranks[neighbor] == discovery_rank - 1:
                continue
            # recurse on neighbors
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)
            # check if edge is a cycle and need to be discarded.
            if recursive_rank <= minimum_rank:
                del self.connection_dict[min(neighbor, node), max(neighbor, node)]
            # update minimum rank if needed
            minimum_rank = min(minimum_rank, recursive_rank)
        return minimum_rank

    def build_adjacency_graph_and_reorganize_connections(self, servers: int, connections: List[List[int]]):

        # initializing for each case
        self.node_ranks = dict()
        self.graph = defaultdict(list)
        self.connection_dict = dict()

        # default ranks for un-initialized nodes is None
        for node in range(servers):
            self.node_ranks[node + 1] = None

        # building adjacency_nodes and re-organizing connections
        for e1, e2 in connections:
            self.graph[e1].append(e2)
            self.graph[e2].append(e1)
            self.connection_dict[(min(e1, e2), max(e1, e2))] = 1


if __name__ == "__main__":
    num_of_servers = 5
    num_of_connections = 5
    connections = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    network = Network()
    print(network.critical_connections(num_of_servers, num_of_connections, connections))