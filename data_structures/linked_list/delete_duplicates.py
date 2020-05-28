
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