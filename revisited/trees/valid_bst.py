class TreeNode:

    def __init__(self, val: int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_valid_via_in_order(self, root: "TreeNode") -> bool:
        """
        Approach: In-order traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        if not root:
            return True

        stack, in_order = [], float("-inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= in_order:
                return False
            in_order = root.val
            root = root.right
        return True

    def is_valid_via_dfs(self, root: "TreeNode") -> bool:
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return True

        def dfs(node, lower=float("-inf"), upper=float("inf")):

            if not node:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False
            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False
            return True

        return dfs(root)

    def is_valid_via_bst(self, root: "TreeNode") -> bool:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue

            if root.val <= lower or root.val >= upper:
                return False

            stack.append(root.right, root.val, upper)
            stack.append(root.left, lower, root.val)
        return True