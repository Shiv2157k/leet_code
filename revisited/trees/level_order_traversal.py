from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val: int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_level_order_traversal(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: Depth First Search
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        def dfs(node: "TreeNode", level: int):

            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return levels

    def get_level_order_traversal_(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: Breadth First Search
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        levels = []
        if not root:
            return levels

        queue, level = deque([root]), 0

        while queue:
            levels.append([])
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)
                levels[level].append(level_nodes)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels

