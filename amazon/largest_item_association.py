from typing import List
from collections import defaultdict


class Items:

    def data_representation(self, items: List[List[str]]):
        unique_items = set()
        items_dict = defaultdict(list)

        for item in items:
            unique_items.add(item[0])
            items_dict[item[0]].append(item[1])
            items_dict[item[1]].append(item[0])
        return items_dict, unique_items

    def largest_chain(self, items: List[List[str]]) -> List[str]:
        """
        Approach:
        :param items:
        :return:
        """
        results = []
        items_graph, nodes = self.data_representation(items)
        visited = set()
        for node in nodes:
            if node in visited:
                continue
            else:
                result = []
                self.dfs(node, items_graph, visited, result)
                if len(results) == 0:
                    results.append(sorted(result))
                elif len(result) > len(results[0]):
                    results = sorted(result)
                elif len(result) == len(results[0]): # Got a candidate
                    results.append(sorted(result))
        return sorted(results)

    def dfs(self, node, items_graph, visited, result):
        visited.add(node)
        for neighbor in items_graph[node]:
            if neighbor in visited:
                continue
            self.dfs(neighbor, items_graph, visited, result)
        result.append(node)


if __name__ == "__main__":
    i = Items()
    print(i.largest_chain(
        [["Item1", "Item2"], ["Item3", "Item4"], ["Item4", "Item5"]]
    ))