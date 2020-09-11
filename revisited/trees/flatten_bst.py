class TreeNode:

    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def flatten(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """

        if not root:
            return root

        node = root

        while node:
            if node.left:
                rightmost = node.left

                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None

            node = node.right
        return node

    def flatten_(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Comlexity: O(N)
        :param root:
        :return:
        """

        if not root:
            return root

        if not root.left and not root.right:
            return root

        left_tail = self.flatten_(root.left)
        right_tail = self.flatten_(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail if right_tail else left_tail

