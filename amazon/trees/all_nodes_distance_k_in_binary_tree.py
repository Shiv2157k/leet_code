from collections import defaultdict, deque
from typing import List, Dict


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def tree_to_graph(self, root: "TreeNode") -> Dict:
        adj_list = defaultdict(list)
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.left:
                adj_list[curr].append(curr.left)
                adj_list[curr.left].append(curr)
                queue.append(curr.left)
            if curr.right:
                adj_list[curr].append(curr.right)
                adj_list[curr.right].append(curr)
                queue.append(curr.right)
        return adj_list

    def all_nodes_distance_k(self, root: "TreeNode", target: "TreeNode", K: int) -> List[int]:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :param target:
        :param K:
        :return:
        """
        # validations
        if not root or not target:
            return []
        if K <= 0:
            return [target.val]

        # generate adjacency nodes
        adj_list = self.tree_to_graph(root)

        # initialize variables for bfs
        queue = deque([target])
        visited = set()
        result = []
        depth = 0

        while queue and depth <= K:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr not in visited:
                    for child in adj_list[curr]:
                        queue.append(child)
                    if depth == K:
                        result.append(curr.val)
                visited.add(curr)
            depth += 1
        return result
