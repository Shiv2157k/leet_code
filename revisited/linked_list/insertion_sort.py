class ListNode:

    def __init__(self, val: int, next: None or int):
        self.val = val
        self.next =next


class LinkedList:

    def insertion_sort(self, head: "ListNode") -> "ListNode":

        # we need three pointers here, p is the position where curr is gonna
        # insert after
        # curr is element we need to compare each time
        # dummy is to return the sorted list, and in case head is changed
        p = dummy = ListNode(0)
        curr = dummy.next = head

        # traverse to last second node
        while curr and curr.next:
            # compare current val with next node val
            # if sequence is sorted already, keep looking ahead
            next_val = curr.next.val
            if curr.val <= next_val:
                curr = curr.next
                continue

            # if there is an element which is smaller than previous seq
            # we need to find a proper position to insert this small element
            if p.next.val > next_val:
                p = dummy

            # p stops at element which is smaller than next val
            # eg 1->2->5->6->7->4->8->9 --> since 4 is bigger than 1, 2
            # we use p.next.val to compare, hence p would point element 2
            # update: curr would point at 7
            while p.next.val <= next_val:
                p = p.next

            # exchange insertion
            # for the above example, p.next should be curr.next which is 4
            # curr.next.next should concatenate elements in sorted seq
            # curr.next should be curr.next.next which is 8
            new = curr.next
            curr.next = new.next
            new.next = p.next
            p.next = new
            # p.next, cur.next.next, curr.next = curr.next, p.next, curr.next.next
        return dummy.next