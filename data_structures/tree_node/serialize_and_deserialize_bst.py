from typing import List


class TreeNode:
    def __init__(self, val, left: None or str, right: None or str):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Serialization and Deserialization of binary search tree
    Approach: DFS Pre-order traversal
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def serialize(self, root: "TreeNode") -> str:

        def recursive_serialize(tree, string) -> str:
            # base case
            if not tree:
                string += "None,"
            else:
                string += str(tree.val) + ","
                string = recursive_serialize(tree.left, string)
                string = recursive_serialize(tree.right, string)
            return string
        return recursive_serialize(root, "")

    def deserialize(self, data: str) -> "TreeNode":

        def recursive_deserailize(bst: List) -> "TreeNode":

            if bst[0] == "None":
                bst.pop()
                return None

            root = TreeNode(bst[0])
            bst.pop()
            root.left = recursive_deserailize(bst)
            root.right = recursive_deserailize(bst)
            return root

        data_list = data.split(",")
        root = recursive_deserailize(data_list)
        return root

