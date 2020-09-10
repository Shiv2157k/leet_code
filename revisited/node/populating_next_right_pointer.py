from collections import deque


class Node:
    def __init__(self, val: int, left:int=None, right:int=None, next:int=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Trees:

    def process_childs(self, child_node, prev, left_most) -> ("Node", "Node"):
        """
        Process the childs and connects them to its adjacent nodes.
        :param child_node:
        :param prev:
        :param left_most:
        :return:
        """
        # if there is child node
        if child_node:
            # if prev pointer is already set
            # we already found at least one node on next level,
            # set up its next pointer
            if prev:
                prev.next = child_node
            else:
                # else this is a fresh node of the next level
                # set it to the leftmost
                left_most = child_node
            prev = child_node
        return prev, left_most

    def connect_levels(self, root: "Node") -> "Node":
        """
        Approach: BFS
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        # base case
        if not root:
            return root

        # Assign the root as left most.
        # as it does not anything left or right to it.
        left_most = root

        # keep looping through.
        # until we find the last level.
        # nodes of last level won't be having any childs.
        while left_most:
            # prev - to keep track of next level latest node.
            # curr - to keep track of current level latest node.
            prev, curr = None, left_most

            # reset the left most to None
            # once you assign it to current
            # to break the outer loop
            left_most = None

            # Iterate on the nodes in current level using
            # next pointer which is already established through
            # process child method.
            while curr:

                # process both the children and update the prev and
                # left most as necessary.
                prev, left_most = self.process_childs(curr.left, prev, left_most)
                prev, left_most = self.process_childs(curr.right, prev, left_most)

                # Move on to the next node
                curr = curr.next
        return root

    def connect(self, root: "Node") -> "Node":
        """
        Approach: Breadth First Search
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return root

        queue = deque([root, ])

        while queue:

            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i == size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
