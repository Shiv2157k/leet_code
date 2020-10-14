class ListNode:
    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next = next


class LinkedList:

    def has_cycle(self, head: "ListNode") -> bool:
        """
        Approach: Turtle and Hare / Slow Pointer & Fast Pointer
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return False

        turtle, hare = head, head.next

        while turtle != hare:
            if not hare or not hare.next:
                return False
            turtle = turtle.next
            hare = hare.next.next
        return True