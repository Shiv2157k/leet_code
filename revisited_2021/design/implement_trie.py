class TrieNode:
    """
    Class for Trie Node.
    """
    def __init__(self):
        self.child_node = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        T: O(M)
        S: O(M)
        :param word:
        :return:
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_node.get(ch, TrieNode())
            curr_node.child_node[ch] = node
            curr_node = node
        curr_node.is_end = True

    def search(self, word) -> bool:
        """
        Returns True if the word exists else False.
        T: O(M)
        S:: O(1)
        :param word:
        :return:
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_node.get(ch)
            if not node:
                return False
            curr_node = node
        return curr_node.is_end

    def starts_with(self, prefix) -> bool:
        """
        Returns True if a per-fix exists else False.
        T: O(M)
        S:O(1)
        :param prefix:
        :return:
        """
        curr_node = self.root
        for ch in prefix:
            node = curr_node.child_node.get(ch)
            if not node:
                return False
            curr_node = node
        return True


if __name__ == "__main__":
    obj = Trie()
    obj.insert("shiva")
    obj.insert("saga")
    param_2 = obj.search("shiva")
    print(param_2)
    param_3 = obj.starts_with("shiv")
    print(param_3)
    param_4 = obj.starts_with("shin")
    print(param_4)
    print(obj.starts_with("sag"))
