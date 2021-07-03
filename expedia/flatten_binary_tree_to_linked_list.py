class TreeNode:

    def __init__(self, val: int = None, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def flatten_tree(self, node: TreeNode) -> TreeNode:
        """

        :param node:
        :return:
        """

        if not node:
            return None

        if not node.right and not node.left:
            return node

        left_tail = self.flatten_tree(node.left)
        right_tail = self.flatten_tree(node.right)

        if left_tail:
            left_tail.next = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def flatten_to_linked_list(self, root: TreeNode):
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        self.flatten_tree(root)

    def flatten_to_linked_list_(self, root: TreeNode):
        """
        Approach: Morris Traversal
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
                while right_most.right:
                    right_most = right_most.right

                right_most.right = node.right
                node.right = node.left
                node.left = None

            node = node.right
        return root
