from math import inf
from collections import deque


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MinimumDepth:

    def get_min_depth(self, root: TreeNode) -> int:
        """
        Approach: Recursion using DFS
        :param root:
        :return:
        """
        # Base case
        if not root:
            return 0
        nodes = [root.left, root.right]
        if not any(nodes):
            return 1
        min_depth = float(inf)

        for node in nodes:
            if node:
                min_depth = min(self.get_depth(node), min_depth)
        return min_depth

    def get_min_depth_(self, root: TreeNode) -> int:
        """
        Approach: Iterative using DFS
        :param root:
        :return:
        """
        # Base Case
        if not root:
            return 0
        else:
            stack, min_depth = [(root.left, root.right), ], float(inf)

        while stack:
            depth, root = stack.pop()
            min_depth = min(depth, min_depth)
            nodes = [root.left, root.right]
            if not any(nodes):
                min_depth = min(depth, min_depth)
            for node in nodes:
                stack.append((depth + 1, node))
        return min_depth

    def get_min_depth(self, root: TreeNode) -> int:
        """
        Approach: Iterative using BFS
        :param root:
        :return:
        """

        if not root:
            return 0
        else:
            queue = deque([(1, root)])

        while queue:
            depth, root = queue.popleft()
            nodes = [root.left, root.right]
            if not any(nodes):
                return depth
            for node in nodes:
                queue.append((depth + 1, node))