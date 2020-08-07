class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class KGroup:

    def reverse_linked_list(self, head: ListNode, k: int) -> ListNode:
        """
        Reverse the list from k nodes
        :param head:
        :param k:
        :return:
        """
        new_head, pointer = None, head

        while k:

            # to keep the next pointer read
            next_node = pointer.next

            # adding the next node of the pointer
            # to the head
            pointer.next = new_head
            new_head = pointer

            # move to the next node
            pointer = next_node

            k -= 1

        return new_head

    def reverse_k_group_(self, head: ListNode, k: int) -> ListNode:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N/ k)
        :param head:
        :param k:
        :return:
        """
        pointer, count = head, 0

        # verify if there are k nodes
        # left in linked list
        while count < k and pointer:
            pointer = pointer.next
            count += 1

        # if we do, then reverse them
        if count == k:

            # reverse first k nodes of linked list
            #  and get the reversed list head
            reverse_head = self.reverse_linked_list(head, k)

            # now recurse on remaining linked list
            # recursion returns the head of overall processed list
            # we use that and original head of k nodes
            # to re-write the connections
            head.next = self.reverse_k_group_(pointer, k)

            return reverse_head
        return head

    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param k:
        :return:
        """
        # k_tail -> tail of the reversed group
        # new_head -> head of the final, modified ll
        pointer, k_tail, new_head = head, None, None

        # keep going until there are no nodes in the linked list.
        while pointer:

            # keep counting nodes from head
            count, pointer = 0,  head

            # find the head of next k nodes
            while count < k and pointer:
                pointer = pointer.next
                count += 1

            # if we got k nodes equal to count
            # reverse them
            if k == count:

                # reverse the k nodes and get the new head
                rev_head = self.reverse_linked_list(head, k)

                # new head is the head of final linked list
                if not new_head:
                    new_head = rev_head

                # k tail is the tail of previous block of reversed
                # k nodes
                if k_tail:
                    k_tail.next = rev_head

                k_tail = head
                head = pointer

        # attach the final, possibly un-reversed portion
        if k_tail:
            k_tail.next = head

        return new_head if new_head else head