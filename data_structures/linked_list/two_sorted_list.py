class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class TwoSortedList:

    def print_list(self, prehead):
        temp = prehead
        while temp:
            print(temp.val)
            temp = temp.next

    def two_sorted_list(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return self.print_list(prehead)


if __name__ == "__main__":
    res = TwoSortedList()

    # Create Nodes
    l1 = ListNode(1)
    l1.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    four = ListNode(3)
    # Create Link
    l1.head.next = second
    second.next = third
    third.next = four

    # Create second Node
    l2 = ListNode(1)
    l2.head = ListNode(1)
    seconds = ListNode(6)
    thirds = ListNode(4)
    # Create Link
    l2.head.next = seconds
    seconds.next = thirds

    print(res.two_sorted_list(l1, l2))
    print(res.print_list(l1))
