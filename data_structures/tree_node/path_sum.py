from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSum:

    def is_path_sum(self, root: TreeNode, target: int) -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """

        # Base Cases
        if not root:
            return False

        target -= root.val

        if not root.left and not root.right:
            return target == 0
        return self.is_path_sum(root.left, target) or \
            self.is_path_sum(root.right, target)

    def is_path_sum_(self, root: TreeNode, target: int) -> bool:
        """
        Approach: Iteration using stack.
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """

        if not root:
            return False
        else:
            stack = [(root, target - root.val), ]

        while stack:
            curr_sum, root = stack.pop()

            if not root.left and not root.right and curr_sum == 0:
                return True
            if root.left:
                stack.append((root.left, curr_sum - root.left.val))
            if root.right:
                stack.append((root.right, curr_sum - root.right.val))
        return False

    def recurse_tree(self, node: TreeNode, remaining_sum: int, path_nodes: List[int], paths_list: List[int]):

        if not node:
            return None

        path_nodes.append(node.val)

        if remaining_sum == node.val and not node.left and not node.right:
            paths_list.append(list(path_nodes))
        else:
            self.recurse_tree(node.left, remaining_sum - node.val, path_nodes, paths_list)
            self.recurse_tree(node.right, remaining_sum - node.val, path_nodes, paths_list)

        path_nodes.pop()

    def get_path_sums(self, root: TreeNode, target: int) -> List[List[int]]:
        """
        Approach: DFS
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param root:
        :param target:
        :return:
        """
        paths_list = []
        self.recurse_tree(root, target, [], paths_list)
        return paths_list
