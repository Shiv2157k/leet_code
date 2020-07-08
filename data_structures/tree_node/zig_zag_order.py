from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ZigZag:

    def level_order_travesal(self, root: TreeNode) -> List[List[int]]:
        """
        Approach: Breadth First Search
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        from collections import deque as dq

        order = []
        level_nodes = dq()
        if root is None:
            return []

        queue = dq([root, None])
        is_left = True
        while len(queue) > 0:
            curr_node = queue.popleft()

            if curr_node:
                if is_left:
                    level_nodes.append(curr_node.val)
                else:
                    level_nodes.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            else:
                order.append(level_nodes)

                if len(queue) > 0:
                    # Acts as a delimiter
                    queue.append(None)

                level_nodes = dq()
                is_left = not is_left
        return order

    def level_order_travesal(self, root: TreeNode) -> List[List[int]]:
        """
        Approach: Depth First Search
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        if root is None:
            return []

        from collections import deque as dq

        order = []

        def dfs(node, level):
            # if this is the first time visiting level
            # add the curr_node val
            if level >= len(order):
                order.append(dq([node.val]))
            else:
                # append according to the level order
                if level % 2 == 0:
                    order[level].append(node.val)
                else:
                    order[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level + 1)

        dfs(root, 0)
        return order
