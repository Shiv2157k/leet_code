class Node:

    def __init__(self, val, next: "Node"=None, random: "Node"=None):
        self.val = val
        self.next = next
        self.random = random


class RandomLinkedList:

    def __init__(self):
        # tracks if a node was visited or not
        self.visited = {}

    def get_cloned(self, node: "Node") -> "Node":
        # if node exists
        if node:
            # if reference already exists in visited
            # return the node from visited
            if node in self.visited:
                return self.visited[node]
            else:
                # if this is a fresh reference
                # add the reference to the visited
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def deep_copy(self, head: "Node") -> "Node":
        """
        Approach: Iterative with O(N) space
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        # base case
        if not head:
            return head

        curr_node = head
        cloned_node = Node(curr_node.val, None, None)
        self.visited[curr_node] = cloned_node

        while curr_node:

            # clone the random link
            cloned_node.random = self.get_cloned(curr_node.random)
            # clone the next link
            cloned_node.next = self.get_cloned(curr_node.next)

            # keep the curr node and clone node traversal going
            curr_node = curr_node.next
            cloned_node = cloned_node.next
        return self.visited[head]

    def get_copy(self, head: "Node") -> "Node":
        """
        Approach: Iterative with O(1) space
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # base case
        if not head:
            return head

        # Weaving the original and cloned
        original_node = head
        while original_node:
            cloned_node = Node(original_node.val, None, None)

            cloned_node.next = original_node.next
            original_node.next = cloned_node
            original_node = cloned_node.next

        # Link the cloned node random links
        # |4|2|next -> |7|0|next -> |-2|None|None|
        # |4|2|next| -> |4|None|next| -> |7|0|next| -> |7|None|None| -> |-2|None|next| -> |-2|None|None|
        original_node = head
        while original_node:
            original_node.next.random = original_node.random.next if original_node.random else None
            original_node = original_node.next.next

        original_list = head
        cloned_list = head.next
        original_head = head.next
        # separate the original and cloned.
        while original_list:

            original_list.next = original_list.next.next
            cloned_list.next = cloned_list.next.next if cloned_list.next else None

            original_list = original_list.next
            cloned_list = cloned_list.next
        return original_head


