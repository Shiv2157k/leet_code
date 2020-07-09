class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FlattenBinaryTree:

    def flatten_tree(self, root: TreeNode) -> TreeNode:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        # validation
        if not root:
            return None
        # base case
        if not root.left and not root.right:
            return root

        left_tail = self.flatten_tree(root.left)
        right_tail = self.flatten_tree(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail if right_tail else left_tail

    def flatten(self, root: TreeNode) -> TreeNode:
        return self.flatten(root)

    def flatten_(self, root: TreeNode) -> TreeNode:
        """
        Approach: O(1) Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        if not root:
            return None

        node = root
        while node:

            if node.left:
                right_most = node.left
                while right_most.next:
                    right_most = right_most.next

                right_most.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
        return node