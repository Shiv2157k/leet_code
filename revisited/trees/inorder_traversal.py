class TreeNode:

    def __init__(self, val:int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def in_order_traversal_(self, root: "TreeNode"):
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        pre, curr = None, root
        in_order = []

        while curr:
            if not curr.left:
                in_order.append(curr.val)
                # move to next right node.
                curr = curr.right
            else:  # has a left sub tree.
                pre = curr.left
                while pre.right:  # find the right most.
                    pre = pre.right
                # put the current after the pre node i.e., build a link.
                pre.right = curr
                # store curr node
                temp = curr
                # move curr node to top of the new tree
                curr = curr.left
                # mark the original current node left to be null,
                # for avoiding infinite loops.
                temp.left = None
        return in_order

    def in_order_traversal(self, root: "TreeNode"):
        """
        Approach: Using stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        stack, in_order = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            in_order.append(root.val)
            root = root.right
        return in_order