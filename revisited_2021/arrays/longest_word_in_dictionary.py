from typing import List


class Dictionary:

    def longest_word(self, words: List[str]) -> str:
        """
        Approach: Using Trie DS
        Time Complexity:O(∑w i)
        Space Complexity: O(∑w i)
        :param words:
        :return:
        """
        from collections import defaultdict
        from functools import reduce
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend(cur[letter] for letter in cur if letter != END)
        return ans

    def longest_word_(self, words: List[str]) -> str:
        """
        Approach: Brute Force
        Time Complexity:O(∑w i2)
        Space Complexity: O(∑w i2)
        :param words:
        :return:
        """
        word_set = set(words)
        words.sort(key=lambda x: (-len(x), x))

        for word in words:
            if all(word[:k] in word_set for k in range(1, len(word))):
                return word
        return ""


if __name__ == "__main__":
    dictionary = Dictionary()
    print(dictionary.longest_word(["w", "wo", "wor", "worl", "world", "worlds"]))
    print(dictionary.longest_word_(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print(dictionary.longest_word_(["w", "wo", "wor", "worl", "world", "worlds"]))
    print(dictionary.longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
