class ListNode:
    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next = next


class LinkedList:

    def delete_duplicates(self, head: "ListNode") -> "ListNode":
        """
        Approach: Pointer
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        new_head = dummy = ListNode(0)

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                dummy.next = head
            else:
                head = head.next
                dummy = head.next
        return new_head.next

