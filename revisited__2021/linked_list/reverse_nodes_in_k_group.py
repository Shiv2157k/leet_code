class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_k_groups(self, head: "ListNode", k: int) -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param k:
        :return:
        """
        ptr = head
        ktail = None

        new_head = None

        while ptr:

            count = 0
            ptr = head

            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                rev_head = self.revers(head, k)

                if not new_head:
                    new_head = rev_head
                if ktail:
                    ktail.next = rev_head

                ktail = head
                head = ptr

        if ktail:
            ktail.next = head

        return new_head if new_head else head

    def reverse(self, head: "ListNode", k: int) -> "ListNode":
        """
        Reverse k nodes
        :param head:
        :param k:
        :return:
        """

        new_head, ptr = None, head

        while k:

            next_node = ptr.next

            ptr.next = new_head
            new_head = ptr

            ptr = next_node
            k -= 1
        return new_head

    def reverse_k_nodes(self, head: "ListNode", k: int) -> "ListNode":
        """
        Reverse the k nodes.
        :param head:
        :param k:
        :return:
        """

        new_head, ptr = None, head

        while k:

            # for keeping track of the next node
            next_node = ptr.next

            # insert node pointed to by pointer
            # at beginning of reversed list.
            ptr.next = new_head
            new_head = ptr

            # move on to next node
            ptr = next_node
            # decrement the count
            k -= 1

        return new_head

    def reverse_k_group(self, head: "ListNode", k: int) -> "ListNode":
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :param k:
        :return:
        """

        # variable to keep track of each valid group
        count = 0
        # pointer for traversing the linked list
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # if the count is same as k time to reverse the group
        if count == k:

            # reverse the first k nodes of the linked list
            reverse_head = self.reverse_k_nodes(head, k)

            # this will recurse on the remaining linked list
            # also re-wires the connections
            head.next = self.reverse_k_group(ptr, k)

            return reverse_head
        return head


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    linked_list = LinkedList()
    ll = linked_list.reverse_k_group(l, 3)

    while ll:
        print(ll.val)
        ll = ll.next