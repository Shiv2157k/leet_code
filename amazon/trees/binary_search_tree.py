class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.MIN = float("-inf")
        self.MAX = float("inf")

    def is_valid(self, root: "TreeNode") -> bool:
        """
        Approach: DFS
        :param root:
        :return:
        """
        return self.dfs(root, self.MIN, self.MAX)

    def dfs(self, node, minimum, maximum):
        """
        :param node:
        :param minimum:
        :param maximum:
        :return:
        """

        if not node:
            return True

        if node.val < minimum or node.val > maximum:
            return False

        return self.dfs(node.left, minimum, node.val - 1) and self.dfs(node.right, node.val + 1, maximum)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(5)

    bst = BinarySearchTree()
    print(bst.is_valid(root))
    print(bst.is_valid(root1))
