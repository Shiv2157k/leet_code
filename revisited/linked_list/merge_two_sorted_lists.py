class ListNode:
    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        """
        Approach: Recursion
        Time Complexity: O(M + N)
        Space Complexity: O(M + N)
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        elif not l2:
            return l2
        elif l1.val < l2.val:
            l1.next = self.merge_(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_(l1, l2.next)
            return l2

    def merge(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        """
        Approach: Iteration
        Time Complexity: O(M + N)
        Space Complexity: O(1)
        :param l1:
        :param l2:
        :return:
        """
        prehead = ListNode(-1)
        new_head = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                new_head.next = l1
            else:
                new_head.next = l2
            new_head = new_head.next

        new_head.next = l1 if l1 else l2