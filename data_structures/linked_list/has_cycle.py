
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def has_cycle(self, head: ListNode) -> bool:
        """
        Approach: Two Pointers.
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True