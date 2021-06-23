class TreeNode:

    def __init__(self, val:int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def in_order_traversal(self, root: "TreeNode"):

        stack, in_order = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            in_order.append(root.val)
            root = root.right
        return in_order

    def pre_order_traversal(self, root: "TreeNode"):

        stack, pre_order = [root,], []

        while stack:
            root = stack.pop()
            if root:
                pre_order.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return pre_order

    def post_order_traversal(self, root: "TreeNode"):

        if not root:
            return []

        post_order, stack = [], [root,]
        while stack:
            root = stack.pop()
            post_order.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return post_order[::-1]

    def post_order_traversal_dfs(self, root: "TreeNode"):

        if not root:
            return []

        return self.post_order_traversal_dfs(root.left) + self.post_order_traversal_dfs(root.right) + [root.val]

    def is_balanced(self, root: "TreeNode"):

        if not root:
            return True
        return self.check_balance(root)[0]

    def check_balance(self, node):

        if not node:
            return True, -1

        left_balance, left_height = self.check_balance(node.left)
        if not left_balance:
            return False, 0
        right_balance, right_height = self.check_balance(node.right)
        if not right_balance:
            return False, 0
        return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)