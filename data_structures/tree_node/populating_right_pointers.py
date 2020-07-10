
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
                    node.next = queue[0]
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

    def connect_ii(self, root: Node) -> Node:
        """
        Approach: Tree Level Traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return None

        from collections import deque

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
        return root

    def process_child(self, child_node: Node, prev: Node, left_most: Node) -> Node:
        # if the child node exists
        if child_node:
            # if prev is present that is still in the start of the next level
            if prev:
                prev.next = child_node
            else:
                # if this is the first time to next level
                # update the left most
                left_most = child_node
            prev = child_node
        return prev, left_most

    def connect_ii_(self, root: Node) -> Node:
        """
        Approach: Using previously established next pointers.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        # Validation
        if not root:
            return None

        # since level has only root making left most as root
        left_most = root

        # iterate over the left_most
        while left_most:

            # prev tracks latest node on next level
            # curr tracks latest node on current level
            prev, curr = None, left_most

            # This will help in reassigning the left most node
            # of next level and break the loop if a leaf is encountered.
            left_most = None

            # iterate over the current level using next pointers.
            while curr:

                # keep processing the left and right child
                # update the prev and left pointers as necessary
                prev, left_most = self.process_child(curr.left, prev, left_most)
                prev, left_most = self.process_child(curr.right, prev, left_most)

                # move to the next node on same level
                curr = curr.next
        return root