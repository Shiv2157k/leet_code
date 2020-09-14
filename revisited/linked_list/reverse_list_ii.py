class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_via_recursion(self, head: "ListNode", m: int, n: int) -> "ListNode":
        """
        Approach: Recursion by swapping
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :param m:
        :param n:
        :return:
        """

        # validation
        if not head:
            return None

        # left - pointer to traverse front wards using .next
        # right - pointer to traverse back wards with recursive call
        left, right = head, head

        # stop - flag that determines if left and right pointers
        # have crossed or reached the same point.
        stop = False

        # Recurse function to reverse
        def recurse_and_reverse(right: "ListNode", m: int, n: int):
            # making the stop and left global
            # to keep track of its state in recursion.
            nonlocal left, stop

            # base case - if n becomes 1 stop that back track lead
            if n == 1:
                return

            # keep moving the right pointer until n reaches 1
            right = right.next

            # if m is greater than 1 keep moving the left pointer
            # until it is less than 1
            if m > 1:
                left = left.next

            # apply the recursion decreasing m and n by 1
            recurse_and_reverse(right, m - 1, n - 1)

            # if two pointers reached same node of got crossed
            # turn on the stop flag
            if left == right and right.next == left:
                stop = True

            # if the flag is off
            # keep swapping the left and right elements
            if not stop:
                left.val, right.val = right.val, left.val
                # keep moving the left pointer
                left = left.next
        recurse_and_reverse(right, m, n)
        return head

    def reverse_via_iteration(self, head: "ListNode", m: int, n: int) -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param m:
        :param n:
        :return:
        """
        # validation
        if not head:
            return None

        # prev - keep track of prev node
        # curr - keep track of curr node
        curr, prev = head, None

        # iteratively move to the starting point of node
        # where we would like to start the reverse.
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n -1

        # con and tail to fix the last connections
        con, tail = prev, curr

        # do the reversing iteratively
        while n:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr
        return head