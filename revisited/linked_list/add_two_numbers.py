class ListNode:
    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next = next


class LinkedList:

    def add_two_linked_list(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        """
        Approach: School Book addition / Elementary Math
        Time Complexity: O(max(l1, l2))
        Space Complexity: O(max(l1, l2))
        :param l1:
        :param l2:
        :return:
        """
        l3 = ListNode(None)
        tail = l3
        carry = 0

        while l1 or l2 or carry:

            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            carry, val = divmod(val1 + val2 + carry, 10)
            tail.next = ListNode(val)
            tail = tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return l3.next