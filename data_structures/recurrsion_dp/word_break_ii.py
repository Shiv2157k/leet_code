from typing import List
from collections import defaultdict


class WordBreak:

    def get_non_empty_list_of_words(self, string: str, word_dict: List) -> List[str]:
        """
        Approach: Recursion (DFS) with memoization
        Time Complexity: O(N^2 + 2^N + W)
        Space Complexity: O(2^N * N + W)
        :param string:
        :param word_dict:
        :return:
        """
        memo = defaultdict(list)
        word_set = set(word_dict)

        def _wordbreak_topdown(string: str):
            # base case
            if not string:
                return [[]]
            if string in memo:
                return memo[string]

            for end_index in range(1, len(string) + 1):
                word = string[:end_index]
                if word in word_set:
                    for subscentence in _wordbreak_topdown(string[end_index:]):
                        memo[string].append([word] + subscentence)
            return memo[string]

        _wordbreak_topdown(string)
        return [" ".join(words) for words in memo[string]]


if __name__ == "__main__":
    word_break = WordBreak()
    print(word_break.get_non_empty_list_of_words("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(word_break.get_non_empty_list_of_words("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

