import heapq

from typing import List
from collections import defaultdict


class TrieNode:

    def __init__(self, val: str = ""):
        self.val = val
        self.children = defaultdict(TrieNode)
        self.heap = []

    def add_child(self, word: str, weight: int):
        heapq.heappush(self.heap, (-weight, word))

    def get_child(self, top: int = 1) -> List[str]:
        prefixes = []
        while self.heap and top:
            _, word = heapq.heappop(self.heap)
            top -= 1
            prefixes.append(word)
        return prefixes


class Dictionary:

    def __init__(self):
        self.trie = TrieNode()

    def add(self, word: str, weight: int):
        node = self.trie
        for char in word:
            node.add_child(word, weight)
            node = node.children[char]

    def search(self, prefix: str, top: int) -> List[str]:
        node = self.trie
        for char in prefix:
            node = node.children[char]
        return node.get_child(top)


if __name__ == "__main__":
    words = Dictionary()
    words.add("amazon", 10)
    words.add("amock", 10)
    words.add("amuck", 10)
    words.add("am", 8)
    words.add("as", 20)
    words.add("ant", 20)
    words.add("amazing", 7)
    words.add("ambiguous", 12)
    words.add("be", 10)
    words.add("bee", 3)
    words.add("bye", 12)
    print(words.search("b", 2))
    print(words.search("a", 3))
    print(words.search("am", 4))