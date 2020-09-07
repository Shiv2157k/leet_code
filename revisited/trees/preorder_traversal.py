from typing import List


class TreeNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class BinarySearchTree:

    def generate_preorder(self, root: "TreeNode") -> List[int]:
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        node, pre_order = root, []
        while node:
            # if there is no left
            # capture the node value
            # move to right
            if not node.left:
                pre_order.append(node.val)
                node = node.right
            else: # if there is left node
                predecessor = node.left

                # move complete right for the predecessor
                # make sure it is not already visited
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                # if this is a new predecessor
                # capture the node value
                # move to left
                if not predecessor.right:
                    pre_order.append(node.val)
                    predecessor.right = node
                    node = node.left
                else: # if there is already a link break and move to right
                    predecessor.right = None
                    node = node.right
        return pre_order

    def generate_preorder_(self, root: "TreeNode") -> List[int]:
        """
        Approach: Iterative using stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        # base case
        if not root:
            return []

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