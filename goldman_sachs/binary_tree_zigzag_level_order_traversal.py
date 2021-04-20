from typing import List
from collections import deque


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ZigZag:

    def level_order_traversal_bfs(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """

        order = []
        level_nodes = deque()
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
            else:
                order.append(level_nodes)
                if len(q) > 1:
                    q.append(None)
                level_nodes = deque()
                is_left = not is_left
        return order

    def level_order_traversal_dfs(self, root: "TreeNode") -> List[List[int]]:
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        order = []
        if not root:
            return order

        def dfs(node: "TreeNode", level: int):

            # if it is a new level
            if level >= len(order):
                order.append(deque([node.val]))
            else:
                if level % 2 == 0: # right to left
                    order[level].append(node.val)
                else: # left to right
                    order[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level + 1)

        dfs(root, 0)
        return order


if __name__ == "__main__":

    n1 = TreeNode(9)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n1.left.left = n4
    n1.left.right = n5
    n1.right.right = n6

    zigzag = ZigZag()
    print(zigzag.level_order_traversal_dfs(n1))

    n11 = TreeNode(9)
    n21 = TreeNode(2)
    n31 = TreeNode(3)
    n41 = TreeNode(4)
    n51 = TreeNode(5)
    n61 = TreeNode(7)
    n11.left = n21
    n11.right = n31
    n11.left.left = n41
    n11.left.right = n51
    n11.right.right = n61

    print(zigzag.level_order_traversal_bfs(n1))