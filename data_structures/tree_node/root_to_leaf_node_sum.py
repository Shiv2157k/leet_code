class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RootToLeaf:

    def get_sum(self, root: TreeNode) -> int:
        """
        Approach: Iterative Pre-order traversal
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        root_to_leaf = 0
        stack = [(root, 0)]
        while stack:
            root, curr_num = stack.pop()
            if root:
                curr_num = curr_num * 10 + root.val
                if not root.left and not root.right:
                    root_to_leaf += curr_num
                else:
                    stack.append((root.right, curr_num))
                    stack.append((root.left, curr_num))
        return root_to_leaf

    def get_sum_(self, root: TreeNode) -> int:
        """
        Approach: Recursive Pre-order traversal.
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        def pre_order(r, curr_num):
            nonlocal leaf_to_node
            if r:
                curr_num = curr_num * 10 + r.val
                if not(r.left or r.right):
                    leaf_to_node += curr_num
                else:
                    pre_order(r.right, curr_num)
                    pre_order(r.left, curr_num)

        leaf_to_node = 0
        pre_order(root, 0)
        return leaf_to_node

    def get_sum__(self, root: TreeNode) -> int:
        """
        Approach: Morris Pre-order Traversal
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        # to keep track of curr_num and sum of the root to leaf
        root_to_leaf = curr_num = 0
        # loop until we explore all the leaves
        while root:

            # to get a predecessor go left and keep moving right
            # until you find the leaf and link it to the root.
            if root.left:
                predecessor = root.left
                # for back tracking to starting point
                steps = 1
                # keep moving to right until you find the leaf
                # and build the link
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1
                # when there is not link, link it to the root
                if not predecessor.right:
                    curr_num = curr_num * 10 + root.val
                    predecessor.right = root
                    # move forward
                    root = root.left
                # time to change sub tree to right
                else:
                    # if reached the end of leaf
                    if not predecessor.left:
                        root_to_leaf += curr_num

                    # do the back_track
                    for _ in range(steps):
                        curr_num //= 10
                    # break the link
                    predecessor.right = None
                    root = root.right
            # if there is no left child go to the right
            else:
                curr_num = curr_num * 10 + root.val
                if not root.right:
                    root_to_leaf += curr_num
                root = root.right
        return root_to_leaf



