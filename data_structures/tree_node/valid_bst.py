class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def is_valid(self, root: TreeNode) -> bool:
        """
        Approach: DFS (Recursion)
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """

        def helper(node, lower=float("-inf"), upper=float("inf")) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)

    def is_valid_(self, root: TreeNode) -> bool:
        """
        Approach: BFS (Iteration using stack)
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """

        if not root:
            return True

        stack = [(root, float("-inf"), float("inf")), ]

        while stack:
            root, lower, upper = stack.pop()

            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))
        return True

    def is_valid__(self, root: TreeNode) -> bool:
        """
        Approach: Iteration with In-order traversal.
        i.e., Left -> Node -> Right
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        stack, in_order = [], float("-inf")

        while stack or not root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= in_order:
                return False
            in_order = root.val
            root = root.right
        return True

