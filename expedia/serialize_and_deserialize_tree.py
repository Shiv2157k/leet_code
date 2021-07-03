from typing import List


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        def rserialize(root: TreeNode, string: str):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string += rserialize(root.left, string)
                string += rserialize(root.right, string)
            return string
        return rserialize(root, "")

    def deserialize(self, data: str):
        """
        Decodes encoded data to tree.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param data:
        :return:
        """
        def rdeserialize(tree: List[str]):
            if tree[0] == "None":
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