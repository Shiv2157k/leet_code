class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def print_list(self, curr_node=None):
        curr_node = self.head
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next

    def append(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return
        prev_node = self.head
        while prev_node.next:
            prev_node = prev_node.next
        prev_node.next = new_node

    def get_sum(self, list_node_1: ListNode, list_node_2: ListNode) -> ListNode:

        list_node = ListNode(0)
        list_node_tail = list_node
        carry = 0

        while list_node_1 or list_node_2 or carry:

            node_1 = (list_node_1.val if list_node_1 else 0)
            node_2 = (list_node_2.val if list_node_2 else 0)

            # result = node_1 + node_2 + carry % 10
            # carry = node_1 + node_2 + carry // 10
            carry, result = divmod(node_1 + node_2 + carry, 10)

            list_node_tail.next = ListNode(result)
            list_node_tail = list_node_tail.next

            list_node_1 = (list_node_1.next if list_node_1 else None)
            list_node_2 = (list_node_2.next if list_node_2 else None)

        return list_node


if __name__ == "__main__":

    linked_list_1, linked_list_2 = LinkedList(), LinkedList()

    linked_list_1.append(2)
    linked_list_1.append(4)
    linked_list_1.append(3)

    linked_list_2.append(5)
    linked_list_2.append(6)
    linked_list_2.append(4)

    linked_list_1.print_list()
    linked_list_2.print_list()

    linked_list = LinkedList()
    result = linked_list.get_sum(linked_list_1.head, linked_list_2.head)
    # Need to do some work in printing the result.
    linked_list.print_list(result)



