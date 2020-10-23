class ListNode:

    def __init__(self, val: int, next: int):
        self.val = val
        self.next = next


class LinkedList:

    def remove_nth_node_(self, head: "ListNode", n: int) -> "ListNode":
        """
        Approach: One Pass
        Time Complexity: O(L)
        Space Complexity: O(1)
        :param head:
        :param n:
        :return:
        """
        first = head
        second = first

        # go to the nth node from head
        while n:
            n -= 1
            first = first.next

        # if you have reached tail
        # return the next of head
        if first is None:
            return head.next

        # loop through until 1st reaches its end
        # and second reaches the breaking point
        while first.next:
            first = first.next
            second = second.next

        # it is time to skip the index
        second.next = second.next.next
        return head

    def remove_nth_node(self, head: "ListNode", n: int) -> "ListNode":
        """
        Approach: Two Pointers
        Time Complexity: O(L)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # create a dummy
        dummy = ListNode(0)
        dummy.next = head
        length, first = 0, head
        # find the total length of the linked list
        while first:
            first = first.next
            length += 1

        # now go back until you reach to the point where
        # it has to break
        length -= n
        # assign the first to dummy
        first = dummy

        # loop and reach the point
        while length:
            length -= 1
            first = first.next

        # jump the value we need to remove
        first.next = first.next.next
        return dummy.next


