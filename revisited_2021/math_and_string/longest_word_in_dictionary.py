from typing import List


class Dictionary:

    def longest_word_in_dictionary(self, s: str, words: List[str]) -> str:
        """
        Approach: Without sort
        Time Complexity: O(m*n)
        Space Complexity: O(n)
        :param s:
        :param word:
        :return:
        """
        ans = ""
        for word in words:
            w, a = len(word), len(ans)
            if w < a or (w == a and ans < word):
                continue
            pos = - 1
            for char in word:
                pos = s.find(char, pos + 1)
                if pos == -1:
                    break
            if pos != -1:
                ans = word
        return ans


if __name__ == "__main__":
    dictionary = Dictionary()
    print(dictionary.longest_word_in_dictionary("abpcplea", ["ale", "apple", "monkey", "plea"]))
    print(dictionary.longest_word_in_dictionary("abpcplea", ["ale", "apple", "applae", "monkey", "plea"]))
