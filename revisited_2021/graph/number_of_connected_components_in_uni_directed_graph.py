from typing import List

from collections import defaultdict


class Graph:

    def count_connected_components(self, n: int, edges: List[int]) -> int:
        """
        Approach: Iterative DFS
        Time Complexity:
        Space Complexity:
        :param n:
        :param edges:
        :return:
        """
        adj_nodes = defaultdict(list)
        for e1, e2 in edges:
            adj_nodes[e1].append(e2)
            adj_nodes[e2].append(e1)

        un_visited = set([i for i in range(n)])
        connections = 0

        while un_visited:
            stack = [un_visited.pop()]
            while stack:
                curr = stack.pop()
                if curr in un_visited:
                    un_visited.remove(curr)
                stack.extend([node for node in adj_nodes[curr] if node in un_visited])
            connections += 1
        return connections


if __name__ == "__main__":
    graph = Graph()
    print(graph.count_connected_components(5, [[0, 1], [1, 2], [3, 4]]))
    print(graph.count_connected_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))

