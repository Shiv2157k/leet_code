from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Merger:

    def merge_k_linked_lists(self, lists: List[ListNode]) -> ListNode:
        """
        Approach: Using Priority Queue
        Time Complexity: O(N log K)
        Space Complexity:
            - O(n) creating a new linked list
            - O(k) since applies in-place method which costs.
            - O(1) space. And the priority queue costs O(k) space
        :param lists:
        :return:
        """
        head = current = ListNode(0)
        q = PriorityQueue()
        i = 0

        for item in lists:
            if item:
                q.put((item.val, i, item))
                i += 1
        while not q.empty():
            val, _, node = q.get()
            current.next = node
            current = current.next
            node = node.next
            if node:
                q.put((node.val, i, node))
                i += 1
        return head.next

    def merge_k_linked_lists_(self, lists: List[ListNode]) -> ListNode:
        """
        Approach: Using Priority Queue
        Time Complexity: O(N log K)
        Space Complexity:
            - O(n) creating a new linked list
            - O(k) since applies in-place method which costs.
            - O(1) space. And the priority queue costs O(k) space
        :param lists:
        :return:
        """
        head = current = ListNode(0)
        q = PriorityQueue()

        class Wrapper():
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < self.other.node.val

        for item in lists:
            if item:
                q.put(Wrapper(item))
        while not q.empty():
            node = q.get().node
            current.next = node
            current = current.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next

    def merge_k_linked_lists__(self, lists: List[ListNode]) -> ListNode:
        """
        Approach: Brute Force
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param lists:
        :return:
        """
        # put all the node values into a list
        self.nodes = []
        # initialize a list node
        head = current = ListNode(0)
        for ll in lists:
            # loop through each linked list
            while ll:
                # append values
                self.nodes.append(ll.val)
                ll = ll.next
        # loop through sorted values
        for val in sorted(self.nodes):
            # build the nodes and link them
            current.next = ListNode(val)
            current = current.next
        return head.next

