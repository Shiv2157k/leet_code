class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def re_order(self, head: "ListNode") -> "ListNode":
        """
        Approach: Find mid, reverse and merge
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """

        # base case
        if not head:
            return head

        # find the mid node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge the first and reversed second half
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return head