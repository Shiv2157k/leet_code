from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def level_order_traversal_(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels
        next_level = deque([root])

        while root and next_level:
            curr_level = next_level
            next_level = deque()
            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return levels[::-1]

    def level_order_traversal(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: Depth First Search
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        def dfs(node: "TreeNode", level: int):
            """
            Depth First Search from top to bottom.
            :param root:
            :param level:
            :return:
            """
            # end of a level
            # add a new list of that level
            if len(levels) == level:
                levels.append([])

            # add the node value of that level
            levels[level].append(node.val)

            # traverse to the left and right tree
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return levels[::-1]

