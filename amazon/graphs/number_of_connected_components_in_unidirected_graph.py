from typing import List
from collections import defaultdict


class UniDirectedGraph:

    def number_of_connected_components(self, n: int, edges: List[List[int]]) -> int:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param edges:
        :return:
        """
        adjaceny_nodes = defaultdict(list)
        # generate all the adjacency node
        for e1, e2 in edges:
            adjaceny_nodes[e1].append(e2)
            adjaceny_nodes[e2].append(e1)

        not_visited = set([i for i in range(n)])
        connections = 0

        while not_visited:
            stack = [not_visited.pop()]
            while stack:
                curr = stack.pop()
                if curr in not_visited:
                    not_visited.remove(curr)
                stack.extend([node for node in adjaceny_nodes[curr] if node in not_visited])
            connections += 1
        return connections


if __name__ == "__main__":
    uni_directed_graph = UniDirectedGraph()
    print(uni_directed_graph.number_of_connected_components(
        5, [[0, 1], [1, 2], [3, 4]]
    ))
    print(uni_directed_graph.number_of_connected_components(
        5, [[0, 1], [1, 2], [2, 3], [3, 4]]
    ))
