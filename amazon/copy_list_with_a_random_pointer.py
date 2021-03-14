class Node:

    def __init__(self, val: int, next: int, random: int):
        self.val = val
        self.next = next
        self.random = random


class RandomLikedList:

    def __init__(self):
        self.visited = {}

    def get_cloned_node(self, node: "Node"):
        # if node exists
        if node:
            # check and see if it is already visited
            if node in self.visited:
                # just return the already visited
                return self.visited[node]
            else: # create a new node and add it to the visited dictionary
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        # return None if the node doesn't exist.
        return

    def clone_node_iterative(self, head: "Node"):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        # base case
        if not head:
            return head

        # initialize a dummy variable
        old_node = head
        # create new node for cloning
        new_node = Node(old_node.val, None, None)
        # add this into the visited dictionary
        # with key as old node and value as new node
        self.visited[old_node] = new_node
        while old_node:

            new_node.next = self.get_cloned_node(old_node.next)
            new_node.random = self.get_cloned_node(old_node.random)

            # keep moving to next node
            new_node = new_node.next
            old_node = old_node.next
        return self.visited[head]

    def clone_node_recursive(self, head: "Node"):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        # base case
        if not head:
            return None

        # if it is already visited return from
        # the visited dictionary
        if head in self.visited:
            return self.visited[head]

        # create a node for cloning
        node = Node(head.val, None, None)

        # make sure to add this into the visited
        # dictionary to eliminate cycles
        self.visited[head] = node

        # recursively traverse to the random linked list
        node.next = self.clone_node_recursive(head.next)
        node.random = self.clone_node_recursive(head.random)

        return node

    def clone_node(self, head: "Node"):
        """
        Approach: Weaving and Un-weaving
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # Step 1: weaving
        # A -> B -> C
        # A' -> B' -> C'
        # A -> A' -> B -> B' -> C -> C'
        pointer = head
        while pointer:
            new_node = Node(pointer.val, None, None)
            new_node.next = pointer.next
            pointer.next = new_node
            pointer = new_node.next

        # Step 2: connect the random pointers
        pointer = head
        while pointer:
            pointer.next.random = pointer.random.next if pointer.random.next else None
            pointer = pointer.next.next

        # Step 3: un-weave the linked list
        # ie., A -> A' -> B -> B' to A->B and A'->B'
        ptr_old_list = head
        ptr_new_list = head.next
        new_head = head.next

        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next.next else None

            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return new_head

