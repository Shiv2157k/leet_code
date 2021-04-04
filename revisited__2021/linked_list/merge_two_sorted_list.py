class LinkNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def merge_(self, l1: "LinkNode", l2: "LinkNode"):
        """
        Approach: Iterative
        Time Complexity:
        Space Complexity:
        :param l1:
        :param l2:
        :return:
        """
        pre_head = LinkNode(-1)
        prev = pre_head

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return pre_head.next

    def merge(self, l1: "LinkNode", l2: "LinkNode"):
        """
        Approach: DFS
        Time Complexity:
        Space Complexity:
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


if __name__ == "__main__":

    linked_list = LinkedList()
    l1 = LinkNode(1)
    l1.next = LinkNode(3)
    l1.next.next = LinkNode(5)

    l2 = LinkNode(1)
    l2.next = LinkNode(2)
    l2.next = LinkNode(4)
    l3 = linked_list.merge(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next
    l3 = linked_list.merge_(l1, l2)
    print("--------------")
    while l3:
        print(l3.val)
        l3 = l3.next