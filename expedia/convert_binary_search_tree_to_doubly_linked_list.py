class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTToDLinkedNode:

    def convert(self, root: "TreeNode"):
        """
        Approach: In-order DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        def helper(node: "TreeNode"):

            nonlocal first, last

            if node:

                # perform in-order
                # i.e., traverse through left child
                # until we reach leaf node
                helper(node.left)

                # if there is last node
                # perform linking
                if last:
                    last.right = node
                    node.left = last
                else:  # mark the first node after head
                    first = node

                # keep track of last visited node for linking
                last = node
                # perform right child traversal
                helper(node.right)

        if not root:
            return None

        first = last = None
        helper(root)
        # build the circular link
        first.left = last
        last.right = first

        return first

