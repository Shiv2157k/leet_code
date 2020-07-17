from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Preorder:

    def get_list(self, root: TreeNode) -> List[int]:
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return None

        node, preorder = root, []
        while node:
            # if there is no left child
            # append the node val to output
            # and move to right
            if not node.left:
                preorder.append(node.val)
                node = node.right
            # if there is a left child
            else:
                # assign node.left to predecessor
                predecessor = node.left

                # keep going to right if this is a fresh leaf
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                # if you reach the leaf
                if not predecessor.right:
                    # append the node value
                    preorder.append(node.val)
                    # build the psuedo link
                    predecessor.right = node
                    # move node to left
                    node = node.left
                # if you are visiting second time
                else:
                    # break the link
                    predecessor.right = None
                    # move to right of the node
                    node = node.right
        return preorder

    def get_list(self, root: TreeNode) -> List[int]:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return None
        stack, preorder = [root, ], []
        while stack:
            root = stack.pop()
            if root:
                preorder.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return preorder
