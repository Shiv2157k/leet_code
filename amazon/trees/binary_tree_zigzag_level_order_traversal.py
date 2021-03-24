from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ZigZag:

    def level_order_traversal_dfs(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        order = []

        if not root:
            return order

        def dfs(node: "TreeNode", level: int):

            if level >= len(order):  # new level
                order.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    order[level].append(node.val)
                else:
                    order[level].appendleft(node.val)

            # traverse left and right node.
            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level + 1)

        dfs(root, 0)
        return order

    def level_order_traversal_bfs(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(H) H - height of the tree.
        :param root:
        :return:
        """
        order, level_nodes = [], deque()
        if not root:
            return order

        # node and none as delimiter
        q = deque([root, None])
        is_left = True

        while q:
            curr_node = q.popleft()
            if curr_node:
                if is_left:
                    level_nodes.append(curr_node.val)
                else:
                    level_nodes.appendleft(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            else:  # new level
                order.append([level_nodes])
                if len(q) > 0:
                    q.append(None)
                # reset the level node queue
                # is left bool
                level_nodes = deque()
                is_left = not is_left
        return order