class TreeNode:
    def __init__(self, val: int, left:int=None, right:int = None):
        self.val = val
        self.left = left
        self.right = right


class RootToLeaf:

    def get_sum(self, root: "TreeNode") -> int:
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        root_to_leaf = curr_sum = 0

        while root:
            # if the root.left exists build the predecessor
            if root.left:
                # assign predecessor
                predecessor = root.left
                # keep track of the steps to traverse backwards
                steps = 1

                # keep going right of the predecessor,
                # to find the actual predecessor.
                # If it is not linked to root.
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # if there is no link
                if not predecessor.right:
                    curr_sum = curr_sum * 10 + root.val
                    # build the link
                    predecessor.right = root
                    # keep moving left
                    root = root.left
                else:  # if there is  a link already established.
                    if not predecessor.left:
                        root_to_leaf += curr_sum
                    # traverse back
                    for _ in range(steps):
                        curr_sum //= 10
                    # break the link
                    predecessor.right = None
                    # move to right
                    root = root.right
            else:   # if there is no left child, calculate right and keep moving right.
                curr_sum = curr_sum * 10 + root.val
                if not root.right:
                    root_to_leaf += curr_sum
                root = root.right
        return root_to_leaf

    def get__sum(self, root: "TreeNode") -> int:
        """
        Approach: Breadth First Search
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        root_to_leaf = 0
        stack = [(root, 0)]

        while stack:
            root, curr_sum = stack.pop()
            if root:
                curr_sum = curr_sum * 10 + root.val
                if not root.left and not root.right:
                    root_to_leaf += curr_sum
                else:
                    stack.append((root.right, curr_sum))
                    stack.append((root.left, curr_sum))
        return root_to_leaf

    def get___sum(self, root: "TreeNode") -> int:
        """
        Approach: Depth First Search
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        def pre_order(r, curr_sum):
            nonlocal root_to_leaf
            if r:
                curr_sum = curr_sum * 10 + r.val
                if not (r.left or r.right):
                    root_to_leaf += curr_sum
                pre_order(r.right, curr_sum)
                pre_order(r.left, curr_sum)

        root_to_leaf = 0
        pre_order(root, 0)
        return root_to_leaf