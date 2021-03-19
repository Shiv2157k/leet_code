from typing import List
from collections import defaultdict


class ProductIDPairs:

    def into_categories(self, pairs: List[List[int]]):
        """
        Approach: Back Tracking / DFS
        Time Complexity:
        Space Complexity:
        :param pairs:
        :return:
        """

        graph = defaultdict(list)
        for e1, e2 in pairs:
            graph[e1].append(e2)
            graph[e2].append(e1)

        result = []
        visited = set()

        def dfs(node: int, group: List):
            visited.add(node)
            group.append(node)
            #if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, group)

        for node in graph:
            group = []
            if node not in visited:
                dfs(node, group)
                result.append(group)
        return result


if __name__ == "__main__":
    product = ProductIDPairs()
    print(product.into_categories(
        [
            [1, 2], [2, 5], [3, 4], [4, 6], [6, 8], [5, 7], [5, 2], [5, 2]
        ]
    ))
    print(product.into_categories(
        [
            [1, 2], [2, 5], [3, 4], [4, 6], [6, 8], [5, 7], [5, 2], [3, 1]
        ]
    ))