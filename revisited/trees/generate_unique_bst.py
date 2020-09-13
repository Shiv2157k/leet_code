from typing import List


class TreeNode:

    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def generate_all_unique(self, n: int) -> List["TreeNode"]:
        """
        Approach: Recursion
        Time Complexity: O(4^n / n^1/2)
        Space Complexity: O(4^n / n^1/2)
        :param n:
        :return:
        """
        def trees(left, right):

            if left > right:
                return [None, ]

            all_trees = []
            for i in range(left, right + 1):  # pick up a root
                # all possible left subtrees i is chosen to be a root
                left_trees = trees(left, i - 1)
                # all possible right subtrees i is chose to be a root
                right_trees = trees(i + 1, right)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                all_trees.append(curr_tree)
            return all_trees

        return trees(1, n) if n else []