
class Node:

    def __init__(self, val, left, right, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class RightPointer:

    def connect(self, root: Node) -> Node:
        """
        Approach: Level Order Traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return None

        from collections import deque as dq

        queue = dq([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.left = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect_(self, root: Node) -> Node:
        """
        Approach: Using previously established next pointers.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        if not root:
            return None
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                # do the connection 1
                head.left.next = head.right

                # do the next connection
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            left_most = left_most.left
        return root