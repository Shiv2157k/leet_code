class TreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def is_symmetric(self, root: TreeNode):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return True

        from collections import deque

        q = deque([root.left, root.right])

        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            q.append((node1.left, node2.right))
            q.append((node1.right, node2.left))
        return True

    def is_symmetric_(self, root: TreeNode):
        """
        Approach: Recursion or DFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, node1: "TreeNode", node2: "TreeNode"):

        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val) and self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)