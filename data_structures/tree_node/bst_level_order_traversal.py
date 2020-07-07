from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_level_order_traversal(self, root: TreeNode) -> List[List[int]]:
        """
        Approach: Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        if not root:
            return []
        levels = []

        def helper(node, level):

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def get_level_order_traversal(self, root: TreeNode) -> List[List[int]]:
        """
        Approach: Iteration
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        from collections import deque as dq
        queue, level = dq([root, ]), 0
        while queue:
            levels.append([])
            level_nodes = len(queue)
            for _ in range(level_nodes):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels