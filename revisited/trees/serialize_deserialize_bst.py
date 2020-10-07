from typing import List


class TreeNode:

    def __init__(self, val: int, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    """
    Approach: DFS
    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    def serialize(self, root: "TreeNode") -> str:
        """
        Serializes given Binary Search Tree
        :param root:
        :return:
        """
        def rserialize(root: "TreeNode", string: str) -> str:

            # base case
            if not root:
                string += "None,"

            string += str(root.val) + ","
            string = rserialize(root.left, string)
            string = rserialize(root.right, string)
            return string

        return rserialize(root, "")

    def deserialize(self, data: str) -> "TreeNode":
        """
        Deserializes given string into binary search.
        :param data:
        :return:
        """
        def rdeserialize(tree: List[str]) -> "TreeNode":

            if not tree:
                tree.pop(0)
                return None

            root = TreeNode(tree[0])
            tree.pop(0)
            root.left = rdeserialize(tree)
            root.right = rdeserialize(tree)
            return root

        tree_list = data.split(",")
        root = rdeserialize(tree_list)
        return root