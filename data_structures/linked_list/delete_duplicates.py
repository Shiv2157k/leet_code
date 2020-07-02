
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class DeleteDuplicates:

    def delete_duplicates(self, head: ListNode) -> ListNode:

        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.next.val == curr_node.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head

    def delete_duplicates_II(self, head: ListNode) -> ListNode:

        new_head = dummy = ListNode(0)
        new_head.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                dummy.next = head
            else:
                dummy = dummy.next
                head = head.next
        return new_head.next