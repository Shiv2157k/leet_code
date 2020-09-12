from typing import List
from collections import deque as dq


class TreeNode:
    def __init__(self, val: int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class ZigZag:

    def converter(self, root: "TreeNode") -> List[int]:
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        # base case
        if not root:
            return []
        results = []

        # dfs recursion function
        def dfs(node: "TreeNode", level: int):

            # base cas
            if level >= len(results):
                results.append(dq([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level + 1)
        dfs(root, 0)
        return results

    def converter_(self, root: "TreeNode") -> List[int]:
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        # base validation
        if not root:
            return []

        # order - to maintain th zig zag order
        # level node - to maintain the level nodes
        order, level_nodes = [], dq()

        # queue - for bfs traversal
        # None - acts as a delimiter of that level
        queue = dq([root, None])

        # flag to determine left node
        is_left = True

        while queue:
            curr_node = queue.popleft()

            if curr_node:
                if is_left: # append to the tail
                    level_nodes.append(curr_node.val)
                else:
                    level_nodes.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            else:
                # we have came to next level
                order.append(level_nodes)
                if queue:
                    # reset the delimiter
                    queue.append(None)
                # reset the level nodes
                level_nodes = dq()
                # reset the flag
                is_left = not is_left
        return order

