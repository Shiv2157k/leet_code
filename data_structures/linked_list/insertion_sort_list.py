class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class InsertionSort:

    def get_list_(self, head: ListNode) -> ListNode:
        # validation
        if not head or not head.next:
            return head

        pre = dummy = ListNode(0)
        curr = dummy.next = head

        while curr and curr.next:
            val = curr.next.val
            if val > curr.val:
                curr = curr.next
                continue
            if pre.next.val > val:
                pre = dummy
            while pre.next.val < val:
                pre = pre.next
            new = curr.next
            curr.next = new.next
            new.next = pre.next
            pre.next = new
        return dummy.next

    def get_list(self, head: ListNode) -> ListNode:
        # validation
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next, tail = head, head.next
        dummy.next.next = None

        # loop through the second node
        while tail:
            pre_node, curr_node, post_node = dummy, dummy.next, tail.next
            # loop through the current
            while curr_node:
                if tail.val <= curr_node.val:
                    # swap the nodes
                    pre_node.next, tail.next = tail, curr_node
                    break
                pre_node, curr_node = curr_node, curr_node.next
            else:
                pre_node.next, tail.next = tail, None
            tail = post_node
        return dummy.next