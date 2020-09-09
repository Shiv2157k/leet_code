from typing import List


class Node:

    def __init__(self, val: int = 0, neighbors: List = None):
        self.val = val
        self.neighbors = neighbors if not neighbors else []


class Graph:

    def __init__(self):
        self.visited = {}

    def clone_graph_(self, node: "Node") -> "Node":
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param node:
        :return:
        """
        # base case.
        if not node:
            return node
        # if it is already visited return the node.
        if node in self.visited:
            return self.visited[node]

        # clone the node.
        clone_node = Node(node.val, [])

        # add the reference to visited.
        self.visited[node] = clone_node

        # if neighbors exists.
        while node.neighbors:
            # start cloning the neighbors recursively.
            clone_node.neighbors = [self.clone_graph_(n) for n in node.neighbors]

        return clone_node

    def clone_graph_(self, node: "Node"):
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param node:
        :return:
        """

        # base case
        if not node:
            return node
        marked = {}

        from collections import deque
        queue = deque([node, ])
        marked[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in marked:
                    marked[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                marked[n].neighbors.append(marked[neighbor])
        return marked[node]

