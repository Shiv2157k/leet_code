
class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_two_sorted_list(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(M + N)
        Space Complexity: O(1)
        :param l1:
        :param l2:
        :return:
        """
        pre_head = ListNode(None)
        prev = pre_head

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2

        return pre_head.next
