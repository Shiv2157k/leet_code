class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def is_subtree(self, parent: "TreeNode", child: "TreeNode") -> bool:
        """
        Approach: Comparison of Nodes
        Time Complexity: O(MN)
        Space Complexity: O(N)
        :param parent:
        :param child:
        :return:
        """
        return self.traverse(parent, child)

    # step 1: traverse through all nodes of the parents considering
    # each node as a parent
    def traverse(self, parent: "TreeNode", child: "TreeNode") -> bool:
        return parent and (
                    self.equals(parent, child) or self.traverse(parent.left, child) or self.traverse(parent.right,
                                                                                                     child))

    # step 2: check condition if the two node values are same
    def equals(self, parent: "TreeNode", child: "TreeNode") -> bool:
        # base cases
        if not parent and not child:
            return True
        if not parent or not child:
            return False
        return parent.val == child.val and self.equals(parent.left, child.left) and self.equals(parent.right,
                                                                                                child.right)
