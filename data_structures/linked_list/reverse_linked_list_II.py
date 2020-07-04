class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Reverse:

    def reverse_nodes_between(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Approach: Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param head:
        :param m:
        :param n:
        :return:
        """

        # validation
        if not head:
            return
        # take the two pointers
        left, right = head, head
        # boolean to check the left and right face off
        stop = False

        def reverse(right: ListNode, m: int, n: int):
            nonlocal left, stop
            # base case
            if n == 1:
                return
            # keep the right moving by one step
            right = right.next

            # keep the left moving each step
            if m > 1:
                left = left.next

            # Recurse with m and n decremented by 1
            reverse(right, m - 1, n -1)

            # check if the left and right cross their paths
            # turn on the stop
            if left == right or right.next == left:
                stop = True

            # keep swapping until the stop is true
            if not stop:
                left.val, right.val = right.val, left.val
                # keep moving the left node
                left = left.next

        reverse(right, m, n)
        return head

    def reverse_nodes_between(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param m:
        :param n:
        :return:
        """
        # initialize prev and curr
        prev, curr = None, head
        # keep moving prev and curr
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1
        # once reached initialize the conn and tail
        conn, tail = prev, curr
        # do the reverse
        while n:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1
        # get the new head and tail
        if conn:
            conn.next = prev
        else:
            head = prev
        tail.next = curr
        return head

