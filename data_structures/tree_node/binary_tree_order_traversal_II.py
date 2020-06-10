from typing import List
from collections import deque


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, val):
        self.val = TreeNode(val)


class TreeOrderTraversal:

    def tree_order(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        output = []

        # loop through the tree
        while queue:
            # to store each tree level values.
            level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                # pop the top root value.
                root = queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            # append each level value.
            output.append(level)

        for i in range(len(output)):
            print(output[len(output) - 1 - i])
        return reversed(output)

    def tree_order_(self, root: TreeNode) -> List[List[int]]:

        output, queue = [], [root]
        while queue:
            output.append(child.val for child in queue if child)
            queue = [child for node in queue if node for child in (node.left, node.right) if child]
        return output[::-1]


if __name__ == "__main__":
    # Building Binary Tree
    tree = BinaryTree(3)
    tree.val.left = TreeNode(9)
    tree.val.right = TreeNode(20)
    tree.val.right.left = TreeNode(15)
    tree.val.right.right = TreeNode(7)

    # Traversing
    res = TreeOrderTraversal()
    print(res.tree_order(tree.val))
    print(res.tree_order_(tree.val))
