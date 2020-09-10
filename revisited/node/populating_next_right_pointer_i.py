from collections import deque


class Node:

    def __init__(self, val: int, left:int=None, right:int=None, next:int=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class PointerTrees:

    def connect(self, root: "Node") -> "Node":
        """
        Approach: Next pointers O(1) space
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # connection 1
                head.left.next = head.right
                # connections 2
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    def connect_(self, root: "Node") -> "Node":
        """
        Approach: Next pointers stack
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

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return queue

