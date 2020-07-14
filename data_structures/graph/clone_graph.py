class Node:

    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:

    def __init__(self):
        self.visited = {}

    def clone_graph(self, node: 'Node') -> 'Node':
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param node:
        :return:
        """
        if not node:
            return node

        # if it is already visited return the visited node.
        if node in self.visited:
            return self.visited[node]

        # create a clone node for given node
        # we don't have neighbors as of yet.
        clone_node = Node(node.val, [])

        # add the node to visited
        self.visited[node] = clone_node

        # iterate through neighbors to generate clones and prepare
        # list of cloned neighbors to be added to clone node.
        if node.neighbors:
            clone_node.neighbors = [self.clone_graph(n) for n in node.neighbors]
        return clone_node

    def clone_graph_(self, node: 'Node') -> 'Node':
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param node:
        :return:
        """
        if not node:
            return node
        marked = {}
        from collections import deque
        queue = deque([node])
        marked[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in marked:
                    marked[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                marked[n].neighbors.append(marked[neighbor])
        return marked[node]