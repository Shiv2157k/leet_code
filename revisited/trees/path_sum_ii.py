from typing import List


class TreeNode:

    def __init__(self, val:int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class PathSum:

    def get_path_sums(self, root: "TreeNode", sums: int) -> List[List[int]]:
        """
        Approach: DFS
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param root:
        :param sums:
        :return:
        """
        paths = []
        self.recurse(root, sums, [], paths)
        return paths

    def recurse(self, node: "TreeNode", remaining_sum: int, path_nodes: List[int], paths: List[List[int]]):
        # base case
        if not node:
            return node

        path_nodes.append(node.val)
        if remaining_sum == node.val and not node.left and not node.right:
            paths.append(list(path_nodes))
        else:
            self.recurse(node.left, remaining_sum - node.val, path_nodes, paths)
            self.recurse(node.right, remaining_sum - node.val, path_nodes, paths)
        path_nodes.pop()