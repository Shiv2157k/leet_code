from typing import List


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def traversal_(self, root: "TreeNode") -> List[int]:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)

        return levels[::-1]

    def traversal(self, root: "TreeNode") -> List[int]:
        """
        Approach: Iterative/ BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        from collections import deque
        levels = []
        next_level = deque([root])

        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])

            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append([node.left])
                if node.right:
                    next_level.append([node.right])
            return levels[::-1]
