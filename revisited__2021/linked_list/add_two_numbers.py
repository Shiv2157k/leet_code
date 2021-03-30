class LinkedNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def add_two_numbers(self, l1: "LinkedNode", l2: "LinkedNode") -> "LinkedNode":
        """
        Approach: Text Book Addition
        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n))
        :param l1:
        :param l2:
        :return:
        """

        l3 = LinkedNode(None)
        l3_tail = l3
        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10

            l3_tail.next = LinkedNode(val % 10)
            l3_tail = l3_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l3.next


if __name__ == "__main__":

    ll1 = LinkedNode(None)
    val1 = LinkedNode(2)
    val2 = LinkedNode(4)
    val3 = LinkedNode(3)
    ll1.next = val1
    ll1.next.next = val2
    ll1.next.next.next = val3

    ll2 = LinkedNode(None)
    val11 = LinkedNode(5)
    val22 = LinkedNode(6)
    val33 = LinkedNode(4)
    ll2.next = val11
    ll2.next.next = val22
    ll2.next.next.next = val33

    linked_list = LinkedList()
    ll3 = linked_list.add_two_numbers(ll1.next, ll2.next)

    result = []
    while ll3:
        result.append(ll3.val)
        ll3 = ll3.next
    print(result)
